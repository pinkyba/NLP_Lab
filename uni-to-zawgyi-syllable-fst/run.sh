#!/bin/bash

# Demo shell script code of Kayah ASCII to Unicode font conversion
# Last updated: 10 Jan 2020
# Written by Ye Kyaw Thu, LST Lab., NECTEC, Thailand
# How to run: ./run.sh

# you have to prepare a mapping table between ASCII and Unicode manually
# for Kayah language and save is as ./zawgyi-uni-fst.txt
# Don't forget to prepare input and output symbol text files in advance

# Credit to Ye Zarni (Aung@MUA) and Dr. Zar Zar Linn (MIIT) 
# for preparing Kayah ASCII to Kayah Unicode Mapping table
# prepred date: 3 Nov 2019

#run for sentence.txt
python sentence.py $1 > input.fsa.txt

# build ascii-uni.fst model
fstcompile --isymbols=unicode.sym --osymbols=zawgyi.sym ./zawgyi-uni-fst.txt > ./zawgyi-uni.fst

# make PDF
fstdraw --portrait --isymbols=unicode.sym --osymbols=zawgyi.sym ./zawgyi-uni.fst | dot -Tpdf -Gsize=6,3 -Eheadport=e -Etailport=w > zawgyi-uni.fst.pdf

# browse PDF
evince ./zawgyi-uni.fst.pdf

# build input.fsa model
fstcompile --acceptor --isymbols=unicode.sym ./input.fsa.txt > ./input.fsa
echo -e "fstprint ./input.fsa";
fstprint --isymbols=unicode.sym --osymbols=unicode.sym ./input.fsa

# make PDF
fstdraw --portrait --isymbols=unicode.sym --osymbols=unicode.sym ./input.fsa | dot -Tpdf -Gsize=6,3 -Eheadport=e -Etailport=w > input.fsa.pdf
evince ./input.fsa.pdf

# compose
#fstproject input.fsa | fstcompose - ascii-uni.fst | fstproject --project_output > output.fst
#fstcompose Marsman.fst lexicon_opt.fst | fstproject --project_output 
fstcompose  ./input.fsa ./zawgyi-uni.fst | fstproject --project_output > ./output.fst
#exit;
#fstcompose ./input.fsa ./regex.fsa | fstprint --isymbols=my.syms
#--osymbols=my.syms
echo "print output.fst as text";
fstprint --isymbols=unicode.sym --osymbols=zawgyi.sym ./output.fst

echo "change the format:";
fstprint --isymbols=unicode.sym --osymbols=zawgyi.sym ./output.fst | cut -f4 | tr -d '\n' | sed "s/\\\s/ /g" | sed 's/[0-9]\+$//' > ./output-string.txt ;

# reference: ꤗꤟꤢꤩ꤬ꤡꤝꤟꤥ ꤙꤢꤧ ꤠꤢ꤭ ꤟꤟꤢꤧ꤭ ?
# output of FST: ꤗꤟꤢꤩ꤬ꤡꤝꤟꤥ ꤙꤢꤧ ꤠꤢ꤭ ꤟꤟꤢꤧ꤭ ?

# make PDF	
fstdraw --portrait --isymbols=unicode.sym --osymbols=zawgyi.sym ./output.fst | dot -Tpdf > output.fst.pdf
evince ./output.fst.pdf



