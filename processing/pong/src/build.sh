#!/usr/bin/env bash

gcc pong.c -o ../pongc.o
cd pongrs
cargo build
cp target/debug/pongrs ../../pongrs.o
