from os import listdir
import pandas as pd
from django.core.management import BaseCommand

from yelp_reviews.models import DimDate, FactReview


class Command(BaseCommand):
    help = "Load review facts"

    def add_arguments(self, parser):
        parser.add_argument("-f", "--full", action="store_true")

    def handle(self, *args, **options):
        """Populates the DB with review aggregations"""
        # Load the data
        # Calculate daily aggregations
        # Store results into FactReview
        path = "yelp_reviews/YelpReviewCleansed/"

        filepaths = [ path + f for f in listdir(path) if f.endswith('.csv')]
        yr = pd.concat(map(pd.read_csv, filepaths))
        # yr = pd.read_csv(path+'00.csv')
        numcols  = ["funny","cool","useful","stars"]
        # yr['date'] = yr['date'].astype('datetime64[ns]')
        # yr.set_index('review_id',drop=True)
        # #yr.reset_index(drop=True, inplace=True)

        # yr = yr.drop(['user_id','business_id','text','decade','text_length'],axis=1)
        # yr[numcols] = yr[numcols].fillna(0)
        # yr[numcols] = yr[numcols].astype(int)
        # print(yr.head())


        yr.set_index('review_id', drop=True)
        print(yr.dtypes)
        yr[numcols] = yr[numcols].fillna(0)
        yr.dropna()
        yr = yr[yr['user_id'] != None]
        yr = yr[yr['review_id'].str.len() == 22]
        # yr['funny'] = pd.to_numeric(yr['funny'], errors='coerce')
        # yr = yr.dropna(subset=['funny'])
        # yr['useful'] = pd.to_numeric(yr['useful'], errors='coerce')
        # yr = yr.dropna(subset=['useful'])
        # yr['cool'] = pd.to_numeric(yr['cool'], errors='coerce')
        # yr = yr.dropna(subset=['cool'])

        yr['date'] = yr['date'].astype('datetime64[ns]')
        yr[numcols] = yr[numcols].astype(int)
        #yr.to_csv("yr.csv", sep=',')
        print(yr['review_id'].count())
        yr_sum = yr.groupby( ['date'] )["stars", "useful", "funny", "cool"].apply(lambda l: l.sum() )

        yr_sum["count"] = yr.date.value_counts(dropna=True)
        yr_sum = yr_sum.reset_index()
        yr_sum[numcols] = yr_sum[numcols].astype(int)
        yr_sum.dropna()
        yr_sum.to_csv("yr_sum.csv", index=False, sep=',', encoding='utf-8')
        yr_sum.dropna()



        DimDate.objects.all().delete()
        for index, row in yr_sum.iterrows():
            model = DimDate()
            model.date = row['date']
            model.save()
        print(DimDate.objects.all()[0].date)


        FactReview.objects.all().delete()


        for index, row in yr_sum.iterrows():
            model = FactReview()
            #print(DimDate.objects.get(date=row['date']))
            model.date = DimDate.objects.get(date=row['date'])
            model.count = row['count']
            #print(type(row['count']), row['stars'])
            model.stars = row['stars']
            model.stars = row['funny']
            model.useful = row['useful']
            model.cool = row['cool']
            model.save()

        print("My stars are", FactReview.objects.all()[0])