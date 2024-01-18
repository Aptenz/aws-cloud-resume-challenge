# Cloud Resume Challenge - AWS Hosted Application

This website is part of the Cloud Resume Challenge, showcasing my expertise in creating a serverless cloud infrastructure coupled with a CI/CD pipeline.

## Technologies Used

- **Frontend:** Crafted using HTML, CSS, and JavaScript. The website is based on the Cloud Resume Challenge, which challenges participants to create a website running on serverless cloud infrastructure and building a CI/CD pipeline.

- **Hosting & Distribution:** Deployed to an S3 bucket, securely delivered through CloudFront CDN with HTTPS certification, and domain management via Amazon Route 53.

- **CI/CD:** Continuous deployment through GitHub Actions updates both the frontend on the S3 bucket and provisions backend AWS resources using Terraform.

- **Backend:** Managed by AWS Lambda (Python) and interfaces with a DynamoDB table for data updates.

## Explore

Check out the [live demo](https://resume.nicky-code.com/) to interact with the application.
