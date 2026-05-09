from log_parser import load_log

df = load_log('sample.log')
print(df.head())