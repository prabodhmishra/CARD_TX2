#!/bin/bash
online2-tcp-nnet3-decode-faster --samp-freq=8000 \
           --frames-per-chunk=3000 \
           --extra-left-context-initial=0 \
    	   --frame-subsampling-factor=3 \
           --config=exp/tdnn_7b_chain_online/conf/online.conf \
           --min-active=200 \
           --max-active=7000 \
           --beam=15.0 \
           --lattice-beam=6.0 \
           --acoustic-scale=1.0 \
           --port-num=5050 \
           exp/tdnn_7b_chain_online/final.mdl \
           exp/tdnn_7b_chain_online/graph_pp/HCLG.fst \
           exp/tdnn_7b_chain_online/graph_pp/words.txt
