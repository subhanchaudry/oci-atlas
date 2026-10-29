# Data Science notebooks, jobs, and model serving

Reviewed: 2026-10-29 · Basis: documentation review; no live notebooks, training or serving.

## Choose the execution object

| Object | Role | Avoid confusing it with |
| --- | --- | --- |
| Project | Organizes ML assets | A running compute environment |
| Notebook session | Interactive development | A dependable scheduled production batch process |
| Job definition / job run | Reusable operation / specific execution | An editable notebook or a model endpoint |
| Model catalog artifact | Stored model and associated serving material | A live prediction service |
| Model deployment | Serves compatible model artifacts through an endpoint | A generic API for every artifact format |
| Pipeline | Orchestrates ML steps | Proof that the resulting model is useful |

Use jobs for repeatable preparation, training or batch prediction. Use a serving deployment when the application needs request-time predictions. A classical ML workflow need not use a foundation model or dedicated Generative AI cluster.

## Prerequisites that affect execution

Separate operator IAM from notebook/job/deployment access to data, logs, keys/secrets and networking. Inspect the chosen principal mode in the actual runtime. Define compatible package/environment dependencies and native architecture. A notebook that can read a bucket doesn't prove the job or model deployment can.

Private data access requires DNS/routes/security from the service runtime. Inspect artifacts and required files before execution; a model serialization file alone may not supply the serving entry point or environment.

## Working pattern

Navigate through **Data Science → Projects**; inspect `oci data-science ... --help`. Read the project and existing jobs/models before creating replacements. For a job, resolve artifact/version, command arguments, runtime, shape/storage, network, principal, logging and output location. Observe the job run and verify output, rather than treating creation of its definition as completion.

For deployment, confirm artifact/serving compatibility and endpoint access, then perform a bounded prediction with the application caller. Check output contract independently of process health. Keep data/model versions and run identifiers when reproducing a result.

## Updates and cost

Manage notebooks' active/deactivated states with storage retention in mind. A deactivated notebook can retain billable storage. Model artifacts and model deployments have distinct retention and cost lifecycles. Read current shape/capacity and pricing inputs before sizing or promising a cost.

For changes, preserve application contracts and record the artifact/environment revision. Before deleting a project or artifact, enumerate dependent notebooks, runs, deployments and retained data; don't erase shared assets as a side effect of a failed experiment.

## Sources

- [Data Science resource and operating model](https://docs.oracle.com/en-us/iaas/Content/data-science/using/overview.htm)
- [Jobs and job-run use cases](https://docs.oracle.com/en-us/iaas/Content/data-science/using/jobs-about.htm)
- [Data Scientist's guide to OCI](https://docs.oracle.com/en-us/iaas/Content/GSG/Reference/getting-started-as-data-scientist.htm)
