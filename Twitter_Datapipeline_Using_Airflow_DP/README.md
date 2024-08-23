# Airflow-EC2-Data-Processing-Project

**Author:** Dixit Prajapati

## Project Overview

This project demonstrates setting up Apache Airflow on an AWS EC2 instance to process and manage data workflows. The goal is to create a pipeline that processes CSV data using Airflow, with all necessary configurations and deployments carried out on an EC2 instance running Ubuntu.

## Objectives
- Launch an EC2 instance on AWS with Ubuntu OS.
- Install and configure Apache Airflow.
- Upload required files (CSV, DAGs, ETL scripts) to the EC2 instance.
- Run Airflow to manage and execute data processing workflows.
- Access the Airflow UI to monitor and trigger the workflows.

## Technologies Used
- **Amazon EC2**: To host and run Apache Airflow.
- **Apache Airflow**: For orchestrating and managing data workflows.
- **Python**: For scripting and data processing.
- **CSV Files**: Source data to be processed by Airflow.

## Dataset Description
- **CSV Data**: Contains raw data to be processed by the Airflow DAGs.

## Project Setup
### Prerequisites
- AWS account with EC2 access.
- SSH key pair for accessing the EC2 instance.
- Basic knowledge of Airflow and data processing.

### Steps
1. **Create EC2 Instance**: Launch an EC2 instance on AWS with Ubuntu OS.
2. **Connect to EC2 Instance**: Access the EC2 instance via SSH.
3. **Install Airflow**: Run the provided installation script to set up Apache Airflow.
4. **Run Airflow**: Start Airflow using the appropriate command.
5. **Upload Files**: Copy the necessary files (CSV, `twitter_dag.py`, `twitter_etl.py`) to the Airflow directory on the EC2 instance.
6. **Restart Airflow**: Restart Airflow to apply the changes.
7. **Access Airflow UI**: Open the Airflow UI using the EC2 public DNS and port 8080.
8. **Trigger DAG**: Use the Airflow UI to manually trigger and run the DAG.

## Future Enhancements
- Automate the EC2 instance setup and Airflow installation process.
- Implement additional data processing and ETL tasks.
- Enhance the Airflow workflows with more complex data dependencies and error handling.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please open a pull request or raise an issue.

## Contact Information
For any questions or suggestions, please contact:

- **Dixit Prajapati**
- [LinkedIn](https://www.linkedin.com/in/dixit-prajapati) 
- [Portfolio](https://www.dixitprajapati.com)