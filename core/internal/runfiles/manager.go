package runfiles

import (
	"sync"
	"sync/atomic"

	"github.com/wandb/wandb/core/internal/settings"
	"github.com/wandb/wandb/core/pkg/observability"
	"github.com/wandb/wandb/core/pkg/service"
)

// Internal implementation of the Manager interface.
type manager struct {
	persistFn func(*service.Record)
	logger    *observability.CoreLogger
	settings  *settings.Settings

	// Wait group for file uploads.
	uploadWg *sync.WaitGroup

	// Set of files (not directories) to upload later.
	flushSet   map[string]FileInfo
	flushSetMu *sync.Mutex

	// Whether 'Finish' was called.
	isFinished *atomic.Bool
}

func newManager(params ManagerParams) Manager {
	return &manager{
		persistFn: params.PersistFn,
		logger:    params.Logger,
		settings:  params.Settings,

		uploadWg: &sync.WaitGroup{},

		flushSet:   make(map[string]FileInfo),
		flushSetMu: &sync.Mutex{},

		isFinished: &atomic.Bool{},
	}
}

func (m *manager) ProcessRecord(record *service.FilesRecord) {
	if m.isFinished.Load() {
		m.logger.CaptureError("runfiles: called ProcessRecord() after Finish()", nil)
		return
	}

	// TODO
}

func (m *manager) Flush() {
	if m.isFinished.Load() {
		m.logger.CaptureError("runfiles: called Flush() after Finish()", nil)
		return
	}

	m.flushSetMu.Lock()
	defer m.flushSetMu.Unlock()

	for path, info := range m.flushSet {
		// Avoid capturing the loop variables.
		path := path
		info := info

		m.uploadWg.Add(1)
		go func() {
			m.uploadFile(path, info)
			m.uploadWg.Done()
		}()
	}
}

func (m *manager) Finish() {
	// Mark as finished. Do nothing if already finished.
	if m.isFinished.Swap(true) {
		return
	}

	m.Flush()
	m.uploadWg.Wait()
}

func (m *manager) uploadFile(path string, info FileInfo) {
	// TODO
}
