input_file = 'data/in/clusters_messages.txt' # Path to input file
output_file = 'data/out/character_templates.txt' # Path to output file
without_numbers = False # Deletes all numbers at the start [True, False]
equal_min_len = 4 # Minimal lenght to be matched in the matching phase [0, inf]
new_representative_pretext = "cluster representative: " # string of the cluster representative
ignore_line_pretext = ["size: "] # List of the first parts of the lines, which need to be skipped
number_skipped_characters = 18 # Number of characters skipped at the beginning of the lines [0, inf]
