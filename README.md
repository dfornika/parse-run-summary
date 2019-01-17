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
                "lane": 1,
                "surface": "-",
                "tiles": 28,
                "density": {
                              "value": 884,
                              "error": 32
                           },
                "cluster_pf": {
                                "value": 87.29,
                                "error": 1.32
                              },
                "legacy_phasing_rate": 0.142,
                "legacy_prephasing_rate": 0.159,
                "phasing_slope": null,
                "phasing_offset": null,
                "prephasing_slope": null,
                "prephasing_offset": null,
                "reads": 16.14,
                "reads_pf": 14.10,
                "percent_greater_than_q30": 81.74,
                "yield": 4.23,
                "cycles_error": 301,
                "aligned": {
                                "value": 0.98,
                                "error": 0.05
                           },
                "error": {
                                "value": ,
                                "error": 
                         },
                "error_35": {
                                "value": ,
                                "error": 
                            },
                "error_75": {
                                "value": ,
                                "error": 
                           },
                "error_100": {
                                "value": ,
                                "error": 
                             },
                "intensity_c1": {
                                  "value": ,
                                  "error": 
                                }
              },
              {
                "lane":
                ...
              }
              ...
           ]
  "read_2_i": [
                {
                  ...
                }
                ...
              ],
  "read_3_i": [
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
