import logging
import time
from nltk import word_tokenize
from collections import Counter
import statistics
from tqdm.auto import tqdm

logging.basicConfig(level=logging.INFO)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        times = []
        for i in tqdm(range(100)):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            times.append(end - start)
        average = sum(times) / len(times)
        stddev = statistics.stdev(times)
        print(f"{func.__name__} took an average of {average:.6f} seconds with a standard deviation of {stddev:.6f}")
        return result
    return wrapper

@log_decorator
def dict_counter(file:str):
    counter = {}
    with open(file, 'r') as f:
        text = f.read()
        tokenized = text.split()
        for word in tokenized:
            if word in counter:
                counter[word]+=1
            else: counter[word]=1
    return counter

@log_decorator
def python_counter(file:str):
    with open(file, 'r') as f:
        text = f.read()
        tokenized = text.split()
        counter = Counter(tokenized)
    return counter

dict_counter_result = dict_counter('shakespeare.txt')
python_counter_result = python_counter('shakespeare.txt')
