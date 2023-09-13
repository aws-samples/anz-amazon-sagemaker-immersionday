# Deploy R program with Plumber on SageMaker

The core function of the program should be implmented in [deploy.R](./deploy.R) - <code>inference</code> function. By default, the deployment will setup 'application/json' as content type.

## Notebook Intro
* [R_plumber_quick_test.ipynb](./R_plumber_quick_test.ipynb) is to do quick test on your R code with plumber deployment at local.
* [plumber_deployment_on_sagemaker.ipynb](./plumber_deployment_on_sagemaker.ipynb) provides guidance on dockerize your container, push it to Elastic Container Registry (ECR), deploy your code using SageMaker Endpoint service and test the endpoint with boto3 libary. Please make sure provide check the actual created repo in ECR and deployed endpoint name before testing it.
  * Reference link in your AWS console - assumed you are using AWS Sydney Region:
    * ECR Console - https://ap-southeast-2.console.aws.amazon.com/ecr/repositories?region=ap-southeast-2
    * SageMaker Models console - https://ap-southeast-2.console.aws.amazon.com/sagemaker/home?region=ap-southeast-2#/models
    * SageMaker Endpoints console - https://ap-southeast-2.console.aws.amazon.com/sagemaker/home?region=ap-southeast-2#/endpoints