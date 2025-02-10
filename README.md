# Kruiz-Control-Naming-Script
This python script takes the names of everything in its folder and appends "Play 50 nowait" to make it suitable for Kruiz Control random Sound Playing.

 Usage: put all of your files for your trigger into the folder that op.py is in, then run op.py from the command line with "python op.py".

Check opnames.txt for the generated commands for all of the files in the folder. When you put it in Kruiz Control's triggers.txt, make sure that you put Random Equal before it to make the trigger randomly select from the listed commands. 

Making specific random probabilities for files uses the different option for the Random command, "Random Probability," with each file trigger followed by a number specifying its chance.
 You can use whatever number, just be aware that probability will be based on the range that exists, not explicitly a percentage chance out of 100. You can have identical probabilities for items in the same 'tier' of randomness, (SSR, SR, and R could be used with 1, 5, 20).
 
