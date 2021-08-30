import pandas as pd
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    iris_df_highest_freq = None
    iris_df_classwise_mean = None
    iris_df_classwise_median = None

    print("Column wise means:")
    print(iris_df_highest_freq.mean())
    print(iris_df_classwise_mean.mean())
    print(iris_df_classwise_median.mean())


if __name__ == "__main__":
    main()