package corelib

import (
	"github.com/segmentio/encoding/json"

	"github.com/wandb/wandb/core/pkg/service"
)

// Generic item which works with summary and history
type genericItem interface {
	GetKey() string
	GetValueJson() string
}

// Custom unmarshal function to handle Infinity, -Infinity, and NaN
//
// This is a workaround for the fact that when the client receives a
// negative infinity, positive infinity, or NaN, it converts it to a string
// and sends it to this service. For now we will just store it as a string
// and send it as such to the server.
//
// TODO: We should handle these values properly, but in the short-term to avoid
// panics we will just store them as strings.
func Unmarshal(b []byte) (any, error) {
	jsonString := string(b)
	var x interface{}
	switch jsonString {
	case "Infinity", "-Infinity", "NaN":
		x = jsonString
	default:
		err := json.Unmarshal(b, &x)
		if err != nil {
			return nil, err
		}
	}
	return x, nil
}

func JsonifyItems[V genericItem](items []V) (string, error) {
	jsonMap := make(map[string]interface{})

	for _, item := range items {
		value := item.GetValueJson()
		result, err := Unmarshal([]byte(value))
		if err != nil {
			return "", err
		}
		jsonMap[item.GetKey()] = result
	}

	jsonBytes, err := json.Marshal(jsonMap)
	if err != nil {
		return "", err
	}
	return string(jsonBytes), nil
}

func ConsolidateSummaryItems[V genericItem](consolidatedSummary map[string]string, items []V) *service.Record {
	var summaryItems []*service.SummaryItem

	for i := 0; i < len(items); i++ {
		key := items[i].GetKey()
		value := items[i].GetValueJson()
		consolidatedSummary[key] = value
		summaryItems = append(summaryItems,
			&service.SummaryItem{
				Key:       key,
				ValueJson: value})
	}

	record := &service.Record{
		RecordType: &service.Record_Summary{
			Summary: &service.SummaryRecord{
				Update: summaryItems,
			},
		},
	}
	return record
}
