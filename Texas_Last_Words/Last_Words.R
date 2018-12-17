#run on 3_Clean_Corpus_Executed_Last_Words.csv for word frequency and word cloud

install.packages('tm')
install.packages("wordcloud")
install.packages("RColorBrewer")

library(tm)
library(wordcloud)
library(RColorBrewer)

#Loading in the data
getwd()
setwd("/Users/genevievemilliken/Desktop/Texas_Last_Words/")
last_words <- read.csv("3_Clean_Corpus_Executed_Last_Words.csv", stringsAsFactors = FALSE)

#Combining all the last words together
last_words_text <-paste(last_words$Last.Statement, collapse=" ")

#Checking to see if text is combined
head(last_words_text)

#Setting up source and corpus
last_words_source <- VectorSource(last_words_text)
corpus <- Corpus(last_words_source)

#Cleaning the data 
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stripWhitespace)

#remove additonal stop words
corpus <- tm_map(corpus, removeWords, c("thats", "get", "give", "make", "much"))

#Making a document-term matrix
dtm <- DocumentTermMatrix(corpus)
dtm2 <- as.matrix(dtm)

#Finding the most frequent terms
frequency <- colSums(dtm2)
frequency <- sort(frequency, decreasing=TRUE)

#Checking frequency 
str(frequency)
frequency
head(frequency)

#Making a word cloud 
words <- names(frequency)
wordcloud(words[1:150], frequency[1:150], colors = brewer.pal(12, "Paired"))
