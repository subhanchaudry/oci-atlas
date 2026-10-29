# Recipe: train, register, and serve a predictive model

Reviewed: 2026-10-29 · Basis: documentation-based suggested pattern; no live training or model deployment.

## Resolve the ML outcome

Capture target/prediction contract, source data/window, evaluation criterion, batch versus online consumption and required runtime. A predictive ML workflow is not automatically a foundation-model fine-tuning task. Use the customer's existing data/ML platform where suitable; Data Science provides notebook, job, model and serving objects for distinct stages.

## Suggested sequence

1. Resolve training data and authorization from the actual execution context. Record data version/window and avoid training/validation leakage in the chosen split.
2. Use a notebook for development and a job/pipeline for a repeatable execution. Specify code revision, environment, arguments, shape/storage, principal, logs and output location.
3. Observe the run and inspect its outputs and agreed metric. A successful training process doesn't establish that a candidate should replace the current model.
4. Register the selected artifact and compatible serving material. Record algorithm/configuration, environment, data lineage and evaluation evidence alongside the model identity.
5. For batch, execute a versioned prediction job and verify output keys/counts/contract. For online serving, configure a supported model deployment, endpoint access and a bounded request using the application caller.
6. Integrate the requested application/API, with credentials outside source. Record the model/artifact/environment revision used by consumers.

## Change and rollback

Preserve input/output compatibility when changing artifacts. Inspect the service-supported update behavior; don't promise automatic traffic splitting or rollback if it hasn't been configured. Retain the previous version/reference when the deployment process requires it and verify the requested application outcome after change.

For a failed run, inspect the first artifact/environment/data/network error. For serving, inspect input schema, model loading, runtime compatibility and endpoint authorization before retraining. Monitor the model and application signals the customer actually needs; don't claim drift detection was deployed simply because a metrics service exists.

## Cleanup

Enumerate notebooks, jobs/runs, artifacts, endpoints, storage and schedules. Deactivate or remove only requested resources, distinguishing stopped compute from retained storage. Preserve data and shared models according to the chosen ownership/retention intent. See [Data Science](service-data-science.md) for resource boundaries.

## Sources

- [Data Science assets and serving](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
- [Repeatable job execution](https://docs.oracle.com/en-us/iaas/Content/data-science/using/jobs-about.htm)
- [ML lifecycle and model artifacts](https://docs.oracle.com/en-us/iaas/Content/GSG/Reference/getting-started-as-data-scientist.htm)
- [Data Platform and Data Science integration architecture](https://docs.oracle.com/en/solutions/ai-data-platform-data-science-workloads/)
