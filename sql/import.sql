use Grants;

LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/ORG_STATE.unique.csv' INTO TABLE State (name);
LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/ORG_CITY.unique.csv' INTO TABLE City (name);
LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/ORG_COUNTRY.unique.csv' INTO TABLE Country (name);
LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/ORG_DEPT.unique.csv' INTO TABLE Department (name);
LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/terms/PROJECT_TERMS.unique.csv' INTO TABLE Term (name);
LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/grants.csv'
  INTO TABLE Grants
  FIELDS TERMINATED BY ',' ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
    (
      grant_id,
      project_id,
      project_title,
      activity,
      support_year,
      suffix,
      foa_num,
      @project_start,
      @project_end,
      @budget_start,
      @budget_end,
      app_type,
      cfda_code,
      study_section,
      total_cost,
      total_cost_sub_project)
  SET
    project_start = str_to_date(@project_start, '%m/%d/%Y'),
    project_end = str_to_date(@project_end, '%m/%d/%Y'),
    budget_start = str_to_date(@budget_start, '%m/%d/%Y'),
    budget_end = str_to_date(@budget_end, '%m/%d/%Y');