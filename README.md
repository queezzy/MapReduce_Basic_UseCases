# MapReduce_Basic_UseCases

This repository contains two basic Map Reduce code samples.

## The First example is the distributed word count problem

This a foundation example which can help understanding how map reduce works and then apply the principle to bigger problems.
The word count exemple consists on counting the number of occurences of a word in a wide distributed number of documents. The task can be achieved through parallelization and by dividing the problem into two simple tasks which can be done by many nodes in a cluster at the same time. Those tasks are the map and the reduce task. You will find the code in the wordcount directory. The data you can use to test it are in the inputs directory and is called miserables.

## The second example is what we called "The flicker tags".

We have a sample file containing metadata about a lot of photos. When a user take a photot or post a photo, Flickr collect several metadata. Those metadata are explained in the file flicktags/flickrSpecs.txt
The goal is to find, for each country, which are the most frequent tags (a user can assign tags to a photo) used.

There is a file flickrsample in inputs/inputs which can help you test the mapper and the reducer. 
