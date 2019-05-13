# Setup

Add custom Jupyter-Notebook kernel: 

```
$ mkdir -p ~/.local/share/jupyter/kernels/visionary-wafer
```

Create a file `kernel.json` with the following contents:

```json
{
 "display_name": "Python 2 visionary-wafer", 
 "language": "python", 
 "argv": [
  "/path/to/code/kernel_wrapper.sh",
  "-m", 
  "ipykernel_launcher", 
  "-f", 
  "{connection_file}"
 ]
}
```

## Remarks for cluster usage

Start the Jupyter-Notebook using containers on the cluster (helvetica). To access the notebook from the local computer port forwarding is required on the local computer:

```
ssh -L (portFromLocal):localhost:(portFromCluster) hel
```

e.g.

```
ssh -L 8887:localhost:8888 hel
```