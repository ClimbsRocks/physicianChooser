library(ggplot2)
library(data.table)

# I'm assuming that you'll have the raw .csv file saved in your Downloads folder. If not, you'll have to adjust this path.
treatments <- read.csv("~/Downloads/DS\ Product\ Take\ Home\ Data.csv")
treatments <- data.table(treatments)

# To look at different subsets of the population by health_risk_assessment, simply change the numbers "7,8,9,10" to reflect which health_risk_assessment scores you're intersted in investigating!
# Based on the regression coefficients I saw, my bins are 1-2, 3-4, 5-6, and 7 - 10
patients_subset <- treatments[health_risk_assesment %in% c(7,8,9,10), .(Count = .N, Failures = sum(outcome == 'failure'), SuccessRate = sum(outcome!= 'failure') / .N ), by = .(servicing_provider_id)]

ggplot(patients_subset, aes(x = servicing_provider_id, y = SuccessRate)) +
  geom_point(aes(size = Count)) +
  geom_text(aes(label = servicing_provider_id, vjust = -1.5))

