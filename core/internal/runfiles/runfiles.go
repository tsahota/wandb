// Deals with the saved files of a W&B run.
//
// This includes files saved via `wandb.save(...)` and internally created
// files. It's separate from "artifacts", which is a newer model and exists
// in parallel to this.
package runfiles

import (
	"github.com/Khan/genqlient/graphql"
	"github.com/wandb/wandb/core/internal/filetransfer"
	"github.com/wandb/wandb/core/internal/settings"
	"github.com/wandb/wandb/core/pkg/observability"
	"github.com/wandb/wandb/core/pkg/service"
)

// Manages the files of a run.
type Manager interface {
	// Handles a file save record from a client.
	ProcessRecord(record *service.FilesRecord)

	// Asynchronously uploads all remaining files.
	Flush()

	// Waits for all upload operations finish.
	//
	// Triggers Flush().
	//
	// This must be called after all other method invocations return.
	Finish()
}

type ManagerParams struct {
	// Function for persisting a record to the transaction log.
	PersistFn func(*service.Record)

	Logger       *observability.CoreLogger
	Settings     *settings.Settings
	FileTransfer *filetransfer.FileTransferManager
	GraphQL      graphql.Client
}

func NewManager(params ManagerParams) Manager {
	return newManager(params)
}
