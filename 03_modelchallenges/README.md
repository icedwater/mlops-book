# Production Deployment Challenges

## ML Life Cycle

This is a periodic process beginning with business problem analysis.

- 1. Business Impact
- 2. Data Collection
- 3. Data Preparation
- 4. Feature Engineering
- 5. Model Build/Training
- 6. Test and Evaluation
- 7. Model Deployment
- 8. Monitoring and Optimisation

### Business Impact

Define an idea and its impact on the project, also its complexities, expected results, time required.
Assess the possibilities of an ML solution.

### Data Collection

- What to collect?
- Where to collect from?
- What type of data is it?
- What size is the data?
  - where and how to store it?

#### Challenges

- 3Vs: volume, velocity, variety
- different sources need to be combined?

### Data Preparation

Can occupy a huge chunk of time, author estimates 70-80%

#### Challenges

- missing values
- outliers
- noisy data
- different data formats
- nonstandard data (measurement scales, etc.)

### Feature Engineering

Adjusting the known features or creating new computed features to facilitate ML prediction

Techniques include, among others:
- label encoding
- combining features
- one-hot encoding: converting multiple-choice options to lists
  - e.g. selecting "fish" from ["fish", "beef", "pork", "chicken"] could be represented as [1, 0, 0, 0]
- imputation
- scaling
- log transformation
- removing unwanted features

#### Challenges

- lack of domain knowledge
- creating new features
- deciding which features are useful

### Model Build/Training

- dataset to be segmented into train/validation/test sets (if using supervised learning)
  - test data should not overlap with training or validation sets
  - baseline model can be used to benchmark models from later iterations
    - keep resource requirements (memory, processing speed, time, etc) in mind

#### Challenges

- model complexity
- computational power
- picking a suitable model
- training time

### Test and Evaluation

Pre-production/pre-deployment phase: build test cases and check how model performs.
May be necessary to go back to rebuild and retrain new models.

#### Challenges

- insufficient test data
- picking suitable test
- may need to repeat model build/training
- logging and analysing test results

### Model Deployment

Put the model out in the real world.

- how often to predict?
- how quickly can a predict be made (incl. latency)?
- ML system architecture?
- ML model deployment and maintenance cost?
- infrastructure complexity

#### Challenges

- portability
- scalability
- "data-related"?
- security

### Monitoring and Optimisation

Model performance will degrade over time. Tweaks will need to be made, or the model may
need to be retrained entirely. This retraining can be manually done or automated. Also,
an eye needs to be kept on the input data, as it may not be consistent with the training.

Also keep an eye on infrastructure statistics, such as RAM and storage space, or system
issues, e.g. library versions being upgraded, etc.

#### Challenges

- data drift
- finding the right threshold for various metrics
- anomalies
- finalise and track model evaluation metrics

## Deployment Types

- Batch prediction: use static data to make predictions, save these
  - ML models will need to be updated with new data
  - Pros: affordable, less complex, easy to implement
  - Cons: moderate latency

- Web Service/REST API: predict single record at a time
  - JSON format can be used for input and output
  - Pros: easy to integrate, flexible, fast predictions, can be more economical (pay-what-you-need)
  - Cons: scalability and security issues

- Mobile/Edge Devices: use low-resource devices to make smaller predictions (see [Azure][aiot] or [TinyML][tiny])
  - Pros: lower power requirement, cost-effectiveness, smaller models
  - Cons: complex deployment, lower resource availability

- Real-time: do inference on streaming data
  - can use prediction caching, noSQL databases, or smaller models to cut latency
  - Pros: very low latency
  - Cons: computationally expensive, complex architecture

[aiot]: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/machine-learning-inference-iot-edge
[tiny]: https://hanlab.mit.edu/projects/tinyml

### Non-technical challenges

- Team coordination: different teams may work on different stages of the ML Lifecycle
- Data-related challenges: limited data at dev time vs huge data in production, unseen issues may arise
- Portability: "works on my machine" vs production deployment
- Scalability: may be complex dealing with web-scale interaction
- Robustness: how to deliver error rates close to training scores when in production?
- Security: dealing with data poisoning and/or security

## MLOps

- Adaptation of Development Operations (DevOps) to machine learning - from experiments to production.
- Also involves data engineering and machine learning (see Figure 3.3)
- Includes Continuous Training (CT) alongside (CI/CD)
- Uses automation to improve efficiency and reproducibility
- May require container (e.g. [Podman][podman] or [Docker][docker]) deployment and orchestration (e.g. [Kubernetes][kube5s])

[podman]: https://podman.io
[docker]: https://www.docker.com
[kube5s]: https://kubernetes.io


