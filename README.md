# RandHaps
RandHaps calculates the probability of SNPs encountering by chance 

### Usage

<pre>./RandHaps assoc_file map_file IBDlength rd
</pre>

where:<br>
assoc_file - associated SNPs from GRASP<br>
map_file - Illumina 610k physical map range for each chromosome<br>
IBDlength - length of IBD haplotype<br>
rd - number of random haplotype pairs to be generated<br>


### Input files examples

<pre>
head -5 assoc_file 
CHR	POS
1	2260994
1	2434877
1	2445961
1	2446607
tail -5 assoc_file 
22	50479977
22	50624404
22	50625988
22	50642332
22	50733265
</pre>

<pre>
cat map_file
chr start end
1 742429 247177330
2 8856 242692820
3 38411 199308268
4 63508 191164126
5 91139 180642521
6 110391 170761395
7 140736 158812247
8 166818 146264218
9 36587 140147760
10 114767 135284293
11 189256 134445626
12 64079 132288869
13 18110262 114121252
14 19283777 106358708
15 18421386 100216154
16 37354 88677423
17 51088 78634366
18 59836 76116152
19 217034 63779291
20 11244 62382907
21 9993822 46909175
22 14884399 49524956
</pre>

### Contact

yunusbb@gmail.com<br>
uralub@gmail.com<br>


### Citing

This tool was developed for<br>

Ural Yunusbayev, Albert Valeev, Milyausha Yunusbaeva, Reedik Mägi, Mait Metspalu, Bayazit Yunusbayev. (2019). Reconstructing recent population history while mapping rare variants using haplotypes.<br>

