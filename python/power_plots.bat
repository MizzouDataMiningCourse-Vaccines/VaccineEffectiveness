@echo OFF

python plot.py ../gen_stats/grants_per_city.tsv grants_per_city -v 3 -d \t
python plot.py ../gen_stats/grants_per_county.tsv grants_per_county -v 2 -d \t
python plot.py ../gen_stats/grants_per_state.tsv grants_per_state -v 2 -d \t
python plot.py ../gen_stats/grants_per_pi.tsv grants_per_pi -v 2 -d \t
python plot.py ../gen_stats/funding_per_pi.tsv funding_per_pi -v 2 -d \t