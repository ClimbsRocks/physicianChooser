# Installation & Getting Started
If you don't already have scikit-learn installed:
`pip install -r requirements.txt`

Make sure the "DS Product Take Home Data.csv" file is saved into your Downloads folder (I figured this would be the easiest location for everyone).

To run the regression and see it's sorted results `python findPhysicians.py`.

To see the graph, simply open up `graphingProviders.R` in RStudio. Feel free to change which health_risk_assessment groups you're looking at!

# Methodology

## Regression in Python & scikit-learn
I ran a quick regression on the data to determine the effectiveness of each doctor while taking into account all the other variables that might influence the outcome. 

Based on the coefficients for each doctor, I selected the most effective ones listed one section below. 

## Graphs in R
I was curious whether some doctors might be better with some groups than others. For example, might we find a doctor who specializes in at risk patients, but who isn't great with already healthy ones? Certainly, the most accurate way to do this would be more regressions, but since I like visualizing data, I switched to R for this part. 

The results of our regression test showed that health_risk_assessment was critically important, while gender & age had a relatively minor effect in comparison. This let me simplify the charts to only look at how effective each doctor is for a given at_risk population, without taking into account gender or age. 

We definitely did find doctors who were more or less effective with certain at_risk groups, listed below. 

# Doctors to reach out to

## Regression Results (across all at_risk groups)
66, 78, 22, 89, 92, 38, 65, 5, 79, 84, 45, 69, 28, 64, 47, 11

These results are sorted from most effective to less effective. The entire list (along with their actual coefficients) are listed in your terminal output if you run `python findPhysicians.py`

## health_risk_assessment specialization
These doctors did not make the list above, but are notably more effective among a given health_risk group than their peers. There is certainly a risk of overfitting for the smaller buckets (3,4 and 5,6). The group of doctors who do well with at-risk patients (scoring a 7 or greater on health_risk_assessment) is well worth looking into. 

### At-risk patients (health_risk of 7 - 10):
4, 61, 95, 77, 60, 50, 51, 52, 33

### Medium risk patients (health_risk of 5,6):
71, 42, 80, 7, 28, 17

### Lighter risk patients (health_risk of 3,4):
15, 40, 41, 63


# Desired Future Features
To judge the clinical effectiveness of doctors, I'd primarily seek information in two categories. 

I would seek legal counsel on all of these data points to make sure we're in compliance with regulations. I would also seek intenral guidance from the Privacy team to make sure to stay well within any ethical or moral guidelines established by people far more knowledgeable in these areas than I. 

### Info about the patients
1. Condition-specific physiological data (if dealing with the heart, information like blood pressure, weight, cholesterol, etc.)
1. What medications they're on
1. Any information around the Big 5 personality traits, or other personality/outlook data
1. Any information on social support they have available to them
1. Their success rates in dealing with other chronic conditions in the past
1. Their engagement with previous providers, and how closely they adhered to their treatment plans (prescription drugs, physical therapy visits, follow up appointments, etc.)
1. Activity & fitness levels
1. Advanced demographic data (income, marital status, number of children, zip code, zip + 4, FICO scores, any advanced segmentation models we or an outside vendor has run on our patients, etc.)


### Info about the doctors
1. Years of practice
1. Hospital or practice currently affiliated with
1. Hospitals affiliated with for med school, internship, residency, and any additional education
1. How much continuing education they have received in recent years
1. Demographic information of the doctor (and whether this matches up with their patients or not- empathy is far more essential in some specializations than in others)
1. How many patients the doctor has seen each year, on average
1. How many and what areas the doctor specializes in, and whether this condition is one of their specialties
1. Any publicly available reviews of the doctor (building relationships with the patient is sometimes critical in getting patients to open up and share information, adhere to treatment plans, come back in for followups, etc.)
1. Adherence to the latest guidelines and research when choosing treatment plans (given a patient with a certain profile, what do the guidelines recommend for treating that patient, and does the doctor follow those guidelines?)

To determine which doctors to reach out to, I would look for the following information outside of clinical effectiviness:
1. Geographic location
1. Weighted transit time to that location by popular modes of transit
1. Whether we have already tried reaching out to this doctor or not
1. Whether this doctor is accepting new patients or not
1. How close the nearest competing doctor in this specialty is (and if they are accepting new patients or not)
1. Lawsuits filed against this doctor, and settlements reached



#### Note on Dates
1. I initially performed feature engineering on the dates and added them in (isWeekend, dayOfWeek, dayOfMonth, monthOfYear, daysSinceFirstDate). Many of them had strong correlations with outcome. However, this seems relatively unlikely to be causative (do we really have reason to believe that the 22nd of a month will produce different outcomes than the 21st of the month?). Ideally, this is something that could be discussed with clinical staff to see if there's any logical explanation for why one month might be more effective than another month (this condition might respond to weather, or general activity levels which probably decline durin winter). At the moment, since it appears to be relatively random and is likely just overfitting to our training data, I removed Dates from consideration, and found no decrease in model accuracy. 

