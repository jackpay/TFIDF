from __future__ import division
import os,math

def tfidf(inDir,outDir,delim="\t"):
    docList = os.listdir(inDir)
    n = len(docList)
    docFreq = dict()
    for docStr in docList:
        tokenSet = set()
        doc = open(inDir + "/" + docStr, "r")
        tokens = doc.read().split(delim)
        doc.close()
        for token in tokens:
            tokenSet.add(token)
        for tok in tokenSet:
            if tok in docFreq:
                docFreq[tok] += 1
            else:
                docFreq[tok] = 1

    for docStr in docList:
        termFreq = dict()
        doc = open(inDir + "/" + docStr, "r")
        tokens = doc.read().split(delim)
        doc.close()
        sToks = len(tokens)
        for token in tokens:
            if token in termFreq:
                termFreq[token] += 1
            else:
                termFreq[token] = 1

        output = open(outDir + "/" + docStr, 'w')
        for token in tokens:
            tf = termFreq[token] / sToks
            idf = math.log((n/docFreq[token]),2)
            tfidf = tf*idf
            if token != "":
                output.write(token + "-<" + str(tfidf) + ">" + delim)

        output.close()

if __name__ == "__main__":
    inD = "/Volumes/BackupHD/Phd-LDA/JGibbOutput/parsed/tok-pos/20-05-2014"
    outD = "/Volumes/BackupHD/Phd-LDA/JGibbOutput/tfidf"
    tfidf(inD,outD)

