#!/bin/bash

for i in {30..40}
do
    for j in {1..5}
    do
        python main.py --map_size 10 --num_humans "$i" --num_vampires "$j" --num_timesteps 10 >> logs.txt
        echo "Done with main.py"
    done
done
