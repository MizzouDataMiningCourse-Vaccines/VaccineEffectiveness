use Grants;

LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/NOCON_PI.unique.csv' INTO TABLE PI_Grant FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (grant_id,pi_id);
#LOAD DATA INFILE '/home/action/workspace/VaccineEffectiveness/data_csv/IC.unique.csv' INTO TABLE IC (name);
