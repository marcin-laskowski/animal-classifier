# Animal Classifier
Deploy animal classifier using [cortex](https://github.com/cortexlabs/cortex).

## Files
```bash
.
├── cortex.yaml                 # model config 
├── predictor.py                # main file with Python class
├── requirements.txt            # regs needed to recreate env
├── sample.json                 # input data sample
└── ...                         # additional files
```

## Local
```bash
# Install cortex
bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/0.19/get-cli.sh)"

# Deploy model from the animal-classifier directory
cortex deploy

# Check status of the deployment (needs to be: live)
cortex get --watch

# Check model PORT when alive
cortex get animal-classifier

# Run model
curl http://localhost:8892 -X POST -H "Content-Type: application/json" -d @sample.json

# Check logs
cortex logs animal-classifier

# Remove model
cortex delete animal-classifier

```

