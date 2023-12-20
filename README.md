# Power BI Employee Resignation Analysis

<img width="960" alt="Rsigning Image PowerBI" src="https://github.com/SurajSanap/Employee-Resigning-Analysis-PowerBI-Dashboard/assets/101057653/0bcfb96a-81b3-4e45-9354-eacc232f8eec">


## Overview

This Power BI dashboard is designed to analyze employee resignations based on a dataset generated in XML format using the Python library Faker. The dataset includes information about 300 employees, including their ID, name, department, resignation date, and the reason for resignation.

## Dataset Structure

The XML file follows the structure below for each employee:

```xml
<employee>
  <id>294296</id>
  <name>Bradley Schmitt</name>
  <department>HR</department>
  <resignation_date>2020-07-15</resignation_date>
  <reason>
    <category>Work</category>
    <details>Wanting a different work environment</details>
  </reason>
</employee>
```

- **id:** Employee ID
- **name:** Employee name
- **department:** Department in which the employee works
- **resignation_date:** Date on which the employee resigned
- **reason:** Details about the reason for resignation, including category and additional details

## Power BI Dashboard

The Power BI dashboard provides insightful visualizations to help understand the patterns and reasons behind employee resignations. The key elements of the dashboard include:

1. **Overview:**
   - Total number of resignations
   - Resignation trend over time

2. **Departments:**
   - Resignation distribution by department
   - Top departments with the highest resignation rates

3. **Reason Analysis:**
   - Categorization of resignation reasons
   - Drill-down into specific reasons and their frequencies

4. **Employee Details:**
   - Individual employee details, including ID, name, department, resignation date, and reason

## How to Use

1. **Download the XML File:**
   - Download the XML file containing the employee resignation dataset.

2. **Open Power BI Dashboard:**
   - Open the Power BI dashboard file (.pbix) using Power BI Desktop.

3. **Refresh Data:**
   - If the XML file is moved or updated, refresh the data source in Power BI to reflect the changes.

4. **Explore Visualizations:**
   - Interact with the various visualizations to gain insights into employee resignations.

## Requirements

- Power BI Desktop (Download: [Power BI Desktop](https://powerbi.microsoft.com/desktop/))

## Contributing

Feel free to contribute to the project by providing feedback, reporting issues, or suggesting enhancements. Pull requests are welcome.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- Data generated using [Faker](https://faker.readthedocs.io/en/master/) Python library.

---

**Note:** Ensure that you have the necessary permissions to use and share the data and that you comply with any legal or organizational policies.
