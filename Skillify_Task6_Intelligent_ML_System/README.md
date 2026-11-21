# Final Task: Intelligent ML Systems

## 1. Project Overview

The Intelligent ML Systems project focuses on implementing and evaluating multiple machine learning techniques to solve different types of problems.

The project demonstrates four major areas of machine learning:

1. Classification
2. Clustering
3. Anomaly Detection
4. Reinforcement Learning

The Iris dataset was used for classification, clustering, and anomaly detection, while a custom Grid World environment was developed for reinforcement learning.

## 2. Dataset Description

**Dataset:** Iris Dataset

The Iris dataset contains measurements of three flower species:

- Setosa
- Versicolor
- Virginica

**Dataset Features:**
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

**Initial Dataset Shape:** 150 rows × 5 columns

**Data Preparation:**
- Checked missing values.
- Identified one duplicate record.
- Removed the duplicate record.
- Final dataset contained 149 records.
- Separated features and target labels.
- Applied feature scaling.
- Split data into training and testing sets.

**Training Dataset:** 119 records

**Testing Dataset:** 30 records

No missing values were found in the original dataset.

## 3. Classification Models

Three classification algorithms were implemented and compared:

### A. Logistic Regression
Logistic Regression is a supervised learning algorithm used for classification. It predicts the probability of an observation belonging to a particular class.

### B. Decision Tree
Decision Tree classifies data using a tree-like structure of conditions and decisions.

### C. Random Forest
Random Forest combines multiple decision trees to improve prediction performance and reduce the limitations of individual trees.

### Classification Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 93.33% | 93.33% | 93.33% | 93.33% |
| Decision Tree | 93.33% | 93.33% | 93.33% | 93.33% |
| Random Forest | 93.33% | 93.33% | 93.33% | 93.33% |

All three models achieved the same accuracy.

### Classification Observations

- Setosa was classified correctly in all 10 test samples.
- Versicolor had 9 correct predictions.
- Virginica had 9 correct predictions.
- Each model made two incorrect predictions.

All three models demonstrated similar performance on the selected test set.

**Visualizations:** Confusion matrices and classification reports were generated for all three models.

## 4. Clustering Using K-Means

K-Means clustering was implemented to identify natural groupings in the Iris dataset.

Unlike classification, clustering does not require target labels during training. It groups observations according to similarities in their feature values.

### Implementation

- Applied feature scaling.
- Configured K-Means with three clusters.
- Assigned each observation to a cluster.
- Used PCA to reduce the feature dimensions to two components for visualization.
- Evaluated clustering using the Silhouette Score.

### Results

| Cluster | Observations |
|---|---:|
| Cluster 0 | 52 |
| Cluster 1 | 50 |
| Cluster 2 | 47 |
| **Total** | **149** |

**Silhouette Score:** 0.4607

### Cluster vs Actual Species

| Cluster | Setosa | Versicolor | Virginica |
|---|---:|---:|---:|
| Cluster 0 | 0 | 39 | 13 |
| Cluster 1 | 50 | 0 | 0 |
| Cluster 2 | 0 | 11 | 36 |

### Observations

- Cluster 1 perfectly grouped all 50 Setosa observations.
- Versicolor and Virginica showed some overlap.
- The clustering algorithm successfully identified meaningful patterns in the dataset.

The Silhouette Score of 0.4607 indicates moderate cluster separation.

**Visualization:** PCA-based K-Means clustering visualization with cluster centroids.

## 5. Anomaly Detection Using Isolation Forest

Isolation Forest was implemented to identify unusual observations in the dataset.

Anomaly detection helps identify records that differ significantly from common data patterns.

### Implementation

- Used the four numerical Iris features.
- Applied feature scaling.
- Trained the Isolation Forest algorithm.
- Identified normal and anomalous observations.
- Used PCA for two-dimensional visualization.

### Results

| Category | Observations |
|---|---:|
| Normal | 141 |
| Anomalies | 8 |
| Total | 149 |

**Anomaly Percentage:** 5.37%

### Detected Anomalies

The algorithm identified eight unusual observations at the following dataset indices:

13, 14, 15, 41, 109, 117, 118, 131.

### Observations

Some detected observations had unusually small sepal or petal measurements, while others had relatively large petal measurements.

These records are not necessarily incorrect. They simply differ from the patterns identified by the algorithm.

**Visualization:** Isolation Forest anomaly detection plot using PCA, with normal observations and anomalies displayed separately.

## 6. Reinforcement Learning Using Q-Learning

A custom 4 × 4 Grid World environment was developed to demonstrate Reinforcement Learning.

The objective was to train an agent to navigate from a starting position to a goal while avoiding obstacles.

### Environment Configuration

| Component | Value |
|---|---|
| Grid Size | 4 × 4 |
| Starting Position | (0, 0) |
| Goal Position | (3, 3) |
| Obstacle | (1, 1) |
| Available Actions | Up, Down, Left, Right |

### Reward System

| Event | Reward |
|---|---:|
| Reach Goal | +10 |
| Hit Obstacle | -10 |
| Normal Movement | -1 |

### Q-Learning Configuration

| Parameter | Value |
|---|---:|
| Learning Rate | 0.1 |
| Discount Factor | 0.99 |
| Initial Exploration Rate | 1.0 |
| Minimum Exploration Rate | 0.01 |
| Epsilon Decay | 0.995 |
| Training Episodes | 2,000 |

A Q-table was created with 16 states and four possible actions per state.

### Training Results

The agent initially received negative rewards because it explored the environment randomly.

As training progressed, its average reward improved.

| Metric | Result |
|---|---:|
| First 100 Episodes Average Reward | -25.00 |
| Last 100 Episodes Average Reward | 4.97 |
| Final Exploration Rate | 0.01 |

### Learned Path

After training, the agent successfully learned this route:

(0,0) → (0,1) → (0,2) → (1,2) → (2,2) → (3,2) → (3,3)

The agent reached the goal in six movements without entering the obstacle.

### Reliability Evaluation

The trained agent was tested across 100 episodes without random exploration.

| Evaluation Metric | Result |
|---|---:|
| Total Test Episodes | 100 |
| Successful Episodes | 100 |
| Success Rate | 100% |
| Average Steps | 6.0 |
| Average Reward | 5.0 |

The results demonstrate that the agent learned a consistent and shortest-path strategy for the configured environment.

**Visualizations:**
- Q-Learning training progress graph.
- Learned path in the Grid World environment.

## 7. Overall Project Findings

The project successfully demonstrated four different machine learning approaches.

| Technique | Algorithm | Main Result |
|---|---|---|
| Classification | Logistic Regression | 93.33% accuracy |
| Classification | Decision Tree | 93.33% accuracy |
| Classification | Random Forest | 93.33% accuracy |
| Clustering | K-Means | 0.4607 silhouette score |
| Anomaly Detection | Isolation Forest | 8 anomalies detected |
| Reinforcement Learning | Q-Learning | 100% success across 100 tests |

## 8. Conclusion

The Intelligent ML Systems project provided practical experience with different machine learning techniques and their applications.

Three supervised classification models were trained and evaluated, achieving 93.33% accuracy on the test dataset.

K-Means clustering identified three meaningful groups within the Iris dataset, while Isolation Forest detected eight unusual observations.

Finally, a Q-Learning agent was successfully trained in a custom Grid World environment. It learned to avoid obstacles and reach the destination in the minimum possible number of movements.

Overall, this project improved practical understanding of supervised learning, unsupervised learning, anomaly detection, reinforcement learning, model evaluation, and data visualization.

## 9. Future Improvements

Possible future improvements include:

- Experimenting with additional classification algorithms.
- Comparing different clustering techniques such as DBSCAN and Hierarchical Clustering.
- Evaluating anomaly detection using different algorithms.
- Testing Q-Learning in larger and more complex environments.
- Experimenting with different reward structures and hyperparameters.
- Testing models on larger real-world datasets.

