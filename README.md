# Databricks Delta Table Samples

This is a code sample repository for demonstrating how to perform [Databricks Delta Table](https://docs.databricks.com/delta/delta-intro.html) operations. The source data used the famous [Online Retail Data Set from UCI Machine Learning Repository](http://archive.ics.uci.edu/ml/datasets/online+retail). And the data for 2010 has been segregated into individual CSV or JSON files for daily data merge demonstration.

* Step 1: Create Master Delta Table (One-Off) - Step_1_Create_Master_Delta_Table_OneOff.ipynb/html
* Step 2: Daily Delta Table Merge (Daily Operation), 02122010 as an example - Step_2_Daily_Delta_Table_Merge.ipynb/html
* Step 2 (Optional): Daily Delta Table Merge (Daily Operation) with source file format in JSON, 03122010 as an example - Step_2_Daily_Delta_Table_Merge_JSON.ipynb/html
* Step 3: Time Travel (Optional) - Step_3_Time_Travel_Optional.ipynb/html

Enjoy!





## Notes for how to create secret store in Databricks.
## Connect Databricks with Databicks CLI
1. Configure Databricks CLI to connect to your Databricks workspace instance.
   ```
   databricks configure --token
   ```
2. Enter the Databricks workspace URL (e.g., https://enter-your-own-workspace.azuredatabricks.net/) and Personal Access Token.

## Create new Secret Scope and Key in Databricks
1. List number of secret scopes in your Databricks workspace.
   ```
   databricks secrets list-scopes
   ```
2. Create the new secret scope.
   ```
   databricks secrets create-scope --scope please_enter_your_own_scope_name --initial-manage-principal users
   ```
3. Put the secret into newly created secret scope.
   ```
   databricks secrets put --scope please_enter_your_own_scope_name --key please_enter_your_own_key_name
   ```
4. List number of secret in the secret scope.
   ```
   databricks secrets list --scope please_enter_your_own_scope_name
   ```

