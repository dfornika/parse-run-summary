# parse-run-summary

See `summary.txt` for typical input file

`parse_read_summary()` returns:

```
[
  {                                                                                        
    "level": "Read 1",                                                                     
    "yield": 4.23,                                                                         
    "projected_yield": 4.23,                                                               
    "aligned": 0.98,                                                                       
    "error_rate": 1.42,                                                                    
    "intensity_c1": 110,                                                                   
    "percent_greater_than_q30": 81.74                                                      
  },    
  {
    "level": "Read 2 (I)",
    ...
  },
  ...
]

```

`parse_read_summary_detail()` returns:

```
{
  "read_1": [
              {
                "lane":
                "surface":
                "tiles":
                "density":
                "cluster_pf":
                "legacy_phasing_prephasing_rate":
                "phasing_slope_offset":
                "prephasing_slope_offset":
                "reads":
                "reads_pf":
                "percent_greater_than_q30":
                "yield":
                "cycles_error":
                "aligned":
                "error":
                "error_35":
                "error_75":
                "error_100":
                "intensity_c1":
              },
              {
                "lane":
                ...
              }
              ...
           ]
  "read_2_I": [
                {
                  ...
                }
                ...
              ],
  "read_3_I": [
                {
                  ...
                }
                ...
              ],
  "read_4": [
                {
                  ...
                }
                ...
              ]
}
```
