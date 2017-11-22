wordlist <- ""
f <- file("https://s3.amazonaws.com/2017-dmfa/project-1/holmes.txt")
open(f)
while(length(line <- readLines(f, n=1)) > 0) {
  word <- unlist(strsplit(line,"\\W+|\\d+"))
  wordlist <- c(wordlist,word)
}
lowerword <- tolower(grep("[a-z]|[A-Z]",wordlist,value = TRUE))
sort(table(lowerword),decreasing=T)[1:10]