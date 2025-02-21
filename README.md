# Spotify Analysis Project on AWS

This project analyzes Spotify data using AWS services like **S3**, **Glue**, **Athena**, and **QuickSight**. The goal is to build a **scalable data pipeline** for processing and visualizing insights from Spotify data.

---

## **Project Overview**
The project involves:
1. **Extracting Data**:  
   - Data is sourced from **Kaggle** - [Link](https://shorturl.at/kE142)
.
2. **Staging Raw Data**:  
   - The raw data is stored in an **S3 bucket** for scalable and cost-effective storage.
3. **ETL with AWS Glue**:  
   - AWS Glue is used for **Extract, Transform, Load (ETL)** processes to clean, transform, and prepare the data for analysis.
4. **Data Warehouse**:  
   - The processed data is stored in **S3** as a data warehouse, making it queryable and ready for analysis.
5. **Schema Inference with Glue Crawler**:  
   - A **Glue Crawler** is used to automatically infer the schema of the processed data and create a metadata table in the **AWS Glue Data Catalog**.
6. **Querying Data**:  
   - **AWS Athena** is used to run SQL queries on the processed data and generate insights.
7. **Visualizing Insights**:  
   - **Amazon QuickSight** is used to create interactive dashboards for data visualization.

---

## **Architecture**
Below is the high-level architecture of the project:

<img width="1041" alt="architecture" src="https://github.com/user-attachments/assets/787f650a-ca3c-4b86-a66c-48b05723dbaf" />

---

## **Tools Used**
- **AWS S3**: For storing raw and processed data.
- **AWS Glue**: For ETL processes and schema inference.
- **AWS Glue Crawler**: For automatically inferring the schema of the processed data.
- **AWS Athena**: For querying data using SQL.
- **AWS QuickSight**: For creating interactive dashboards and visualizations.

---

## **Steps to Reproduce**
1. **Data Ingestion**:
   - Extract data from the Kaggle dataset and store it in an S3 bucket (e.g., `s3://spotify-raw-data`).

2. **ETL with AWS Glue**:
   - Create a Glue job to clean and transform the raw data.
   - Store the processed data in another S3 bucket (e.g., `s3://spotify-processed-data`).

3. **Schema Inference with Glue Crawler**:
   - Use a Glue Crawler to infer the schema of the processed data and create a metadata table in the **AWS Glue Data Catalog**.

4. **Query Data with Athena**:
   - Run SQL queries on the processed data using Athena.

5. **Visualize Data with QuickSight**:
   - Create dashboards in QuickSight to visualize insights.

---

## **Glue Crawler**
The **AWS Glue Crawler** plays a crucial role in this project. It automatically scans the processed data stored in S3, infers the schema, and creates a metadata table in the **AWS Glue Data Catalog**. This metadata table is then used by **AWS Athena** to query the data.

### **How Glue Crawler Works**
1. **Data Source**:  
   - The crawler connects to the S3 bucket where the processed data is stored (e.g., `s3://spotify-processed-data`).

2. **Schema Inference**:  
   - It analyzes the data files (e.g., CSV, Parquet) and infers the schema, including column names, data types, and partitions.

3. **Metadata Table**:  
   - The inferred schema is stored as a metadata table in the **AWS Glue Data Catalog**, which acts as a centralized metadata repository.

4. **Querying with Athena**:  
   - Once the metadata table is created, you can use **AWS Athena** to run SQL queries on the data.

---

## **Athena Query**
In the query, you can use any name for the table (e.g., `name`, `artist_id`, or any other name of your choice).  
The `datawarehouse` refers to the folder where your database is stored in the S3 bucket; you can use your preferred name for the folder.  
The `limit` specifies the number of records you want to retrieve. In the example below, only 12 records will be displayed. You can adjust this number to any value, such as 15 or 20, depending on your preference.

```sql
SELECT * FROM datawarehouse LIMIT 12;
```

---

## **Impact and Achievements**
- **Business Impact**:  
  This project provides actionable insights into user listening habits, helping Spotify improve recommendations, target marketing campaigns, and enhance user engagement.

- **Technical Achievements**:  
  - Designed and implemented an **end-to-end data pipeline** using AWS services like S3, Glue, Athena, and QuickSight.  
  - Automated the **ETL process** using AWS Glue, ensuring consistent data quality.  
  - Used **Glue Crawler** to automatically infer the schema and create a metadata table for querying.  
  - Created **interactive dashboards** in QuickSight for data visualization.  

- **Skills Demonstrated**:  
  - **AWS Cloud Expertise** (S3, Glue, Athena, QuickSight).  
  - **Data Engineering** (ETL, data pipelines).  
  - **SQL and Data Analysis**.  
  - **Data Visualization and Communication**.  

- **Personal Growth**:  
  This project helped me deepen my understanding of the **AWS ecosystem** and apply my skills to solve real-world problems.

---

## **How to Run the Project**
1. Clone this repository:
   ```bash
   git clone "copy and paste github project link"
   ```
2. Follow the steps mentioned in the **Steps to Reproduce** section.

---

## **Contributing**
Feel free to contribute to this project by opening issues or submitting pull requests.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
