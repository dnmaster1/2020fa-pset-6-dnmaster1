from luigi import ExternalTask, Task, BoolParameter
from csci_utils.luigi.dasks.target import CSVTarget, ParquetTarget
from csci_utils.luigi.task import Requires, Requirement, TargetOutput

# from pset_5.csci_utils.luigi.dasks.target import CSVTarget, ParquetTarget
# from pset_5.csci_utils.luigi.task import Requires, Requirement, TargetOutput
import sys


class YelpReviews(ExternalTask):
    __version__ = "1.0.0"
    DATA_ROOT = "s3://pset5yelpreviews/"
    # if len(sys.argv) > 1 and sys.argv[1] == "--full":
    #     files = "*.csv"
    # else:
    #     files = "yelp_subset_0.csv"
    files = "*.csv"
    output = TargetOutput(
        file_pattern=DATA_ROOT,
        ext=".parquet",
        target_class=CSVTarget,
        flag=None,
        glob=files,
        storage_options=dict(requester_pays=True),
    )



class CleanedReviews(Task):
    __version__ = "1.0.0"
    subset = BoolParameter(default=True)
    requires = Requires()
    task2 = Requirement(YelpReviews)
    parquet_data = "./yelpdata/"

    output = TargetOutput(file_pattern=parquet_data, ext="", target_class=ParquetTarget)

    def run(self):

        df = self.input()["task2"].read_dask(check_complete=True)


        df = df[(df.user_id.notnull()) & (df.review_id.str.len() == 22)]
        values = {"funny": 0, "cool": 0, "useful": 0, "stars": 0}
        df = df.fillna(value=values)
        df = df.astype({"funny": int, "cool": int, "useful": int, "stars": int})

        self.output().write_dask(collection=df, compression="gzip")


class BySomething(Task):
    __version__ = "1.0.0"

    requires = Requires()
    task3 = Requirement(CleanedReviews)
    # Be sure to read from CleanedReviews locally

    output = TargetOutput(
        file_pattern="./yelpdata/",
        ext=".parquet",
        target_class=ParquetTarget,
        flag=None,
        glob="*.parquet",
        storage_options=dict(requester_pays=True),
    )

    def run(self):
        df = self.input()["task3"].read_dask(
            check_complete=True, column=["year", "stars", "text"]
        )
        df["decade"] = (df["date"].dt.year // 10) % 10
        df["text_length"] = df["text"].str.len()
        by_decade = df[["decade", "text_length"]].groupby("decade").mean().round()
        by_star = df[["stars", "text_length"]].groupby("stars").mean().round()

        df.to_csv("./yelpdata/YelpReviewCleansed/*.csv", index=False, sep=',', encoding='utf-8')

        self.by_decade = by_decade
        self.by_star = by_star
        print(by_decade.compute())
        print(by_star.compute())

    def print_by_decade(self):
        print(self.by_decade.compute())

    def print_by_star(self):
        print(self.by_decade.compute())

