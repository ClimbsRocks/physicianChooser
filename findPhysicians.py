import csv
import os
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

# read in the data as dictionaries. this makes our code manipulating columns easier to read, and means we can use scikit-learn's awesome DictVectorizer
with open(os.path.expanduser('~/Downloads/DS Product Take Home Data.csv')) as input_file:
    input_file = csv.DictReader(input_file)

    data = []
    header_skipped = False
    for row in input_file:
        if header_skipped:
            data.append(row)
        else:
            header_skipped = True

y = []
for row in data:
    # remove features that are duplicative or that will just add noise
    del row['servicing_provider_name']
    del row['event_id']
    del row['member_id']
    # see note in README on dates if interested in why i'm ignoring the date column
    del row['treatment_date']

    # separate out our 'y' values
    if row['outcome'] == 'failure':
        y.append(0)
    else:
        y.append(1)
    del row['outcome']

    # turn the continuous variable into ints, rather than strings, so it will not be one-hot-encoded by DictVectorizer
    row['member_age'] = int(row['member_age'])

vectorizer = DictVectorizer()
data = vectorizer.fit_transform(data)
feature_names = vectorizer.get_feature_names()

# taking hyperparameters found using RandomizedSearchCV within machineJS (the library I built to automate the entire machine learning process, which I used here to find the optimal hyperparameters in a trivially quick manner).
classifier = LogisticRegression(C=0.28, solver='liblinear', n_jobs=-1)

# train the classifier
classifier.fit(data, y)

# get coefficients for each feature from the classifier, and join them with the appropriate feature_name
zipped_results = zip(feature_names, classifier.coef_.tolist()[0])
zipped_results = sorted(zipped_results, key=lambda x: x[1], reverse=True)

# make terminal output prettier:
for pair in zipped_results:
    # we could certainly filter for only servicing_providers, but i like the gut check of seeing how they compare to other features in the output
    print pair[0] + ': ' + str(pair[1])
