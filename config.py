config_setup = {
    "input":"images/",
    "output":"default_filtered_dir/",
    "logfile": "filter.log",
    "filters": [
        "blur:1",
        "grayscale",
        "dilate:21",
        "zeteam"
    ]
}