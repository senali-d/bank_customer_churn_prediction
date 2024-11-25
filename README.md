# Bank customer churn prediction

## Problem Statement

Customer churn, the departure of clients, poses a significant challenge for banks, as retaining existing customers is typically more cost-efficient than acquiring new ones. This analysis aims to create a predictive model to identify customers at risk of leaving by analyzing their profiles and behavior. By identifying these customers in advance, banks can deploy targeted strategies to enhance retention and boost customer satisfaction.

The importance of addressing customer churn in banking lies in its impact on profitability, operational efficiency, and customer satisfaction:

1. Cost Efficiency: Acquiring new customers is significantly more expensive than retaining existing ones. By focusing on retention, banks can reduce marketing and onboarding expenses.
2. Revenue Preservation: Retaining customers helps maintain a steady revenue stream, as loyal customers often contribute more through repeat business, cross-selling, and upselling opportunities.
3. Customer Loyalty: Proactively addressing churn fosters trust and loyalty, which are critical for long-term customer relationships in the competitive banking sector.
4. Enhanced Strategic Decision-Making: Identifying at-risk customers enables banks to tailor retention strategies, such as personalized offers, improved services, or loyalty programs, to meet specific customer needs.
5. Market Competitiveness: Reducing churn ensures a stable customer base, strengthening the bank's position against competitors.
6. Reputation Management: Satisfied customers are less likely to churn and more likely to provide positive referrals, enhancing the bank's reputation.

By developing predictive models to mitigate churn, banks can efficiently allocate resources, improve customer experiences, and achieve sustainable growth.

### Methods and tools available for customer churn prediction

### Steps
1. Collect customer data of account holders at ABC Multinational Bank.
2. Preprocess the data by cleaning, filling missing values, and resampling if necessary.
3. Train the model on the historical data.
5. Validate the model's performance using evaluation metrics.
6. Make prediction.

### Dataset

> https://www.kaggle.com/datasets/gauravtopre/bank-customer-churn-dataset

10,000 data records were used to train the model.

This dataset is for ABC Multistate bank with following columns:

1. customer_id
2. credit_score
3. country
4. gender
5. age
6. tenure
7. balance
8. products_number
9. credit_card
10. active_member
11. estimated_salary
12. churn - used as the target. 1 if the client has left the bank during some period or 0 if he/she has not.

Aim is to Predict the Customer Churn for ABC Bank.

## How to run this project?

### Prerequisites

- Pipenv, Python virtualenv management tool
- docker and docker-compose

### Project Setup

1. Clone the project from repository

``` 
https://github.com/senali-d/bank_customer_churn_prediction.git
cd bank_customer_churn_prediction
```

2. Build the Docker image from Dockerfile

```
docker build -t bank-customer-churn .
```

3. Run the Docker container from the created image

```
docker run -it --rm -p 9696:9696 bank-customer-churn
```

4. Test the model

```
pipenv shell
python predict-test.py 
```

If setup is correct, the following output should be displayed:

```
{'churn': True, 'churn_probability': 0.683151062071004}
```

