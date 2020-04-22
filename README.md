# Engineering stability in gene networks by autoregulation
## Overview
In this project we looked at research paper[1] in which authors have designed and constructed simple gene circuits consisting of a regulator and transcriptional repressor modules and have shown that the gain of stability can be produced by negative feedback. Our object was to produce and analyze the results mentioned in the paper[1]

## Code structure
[vary_kr.py](vary_kr.py) : contains code for variation of Stability Ratio with Binding Constant of the Repressor (k<sub>r</sub>)<br/>
[vary_kp.py](vary_kp.py) : contains code for variation of Stability Ratio with Binding Constant of the Polymerase (k<sub>p</sub>)<br/>
[vary_kI.py](vary_kI.py) : conatins code for variation of Stability Ratio with Isomerization Rate (k<sub>I</sub> ) as well as variation of Stability Ratio with Degradation Rate of Repressor (k<sub>deg</sub>)

## Conclusion
By varying the parameters within a range of values with biological significance we were
able to find range of values for which the autoregulatory system shows a twofold increase
in stability over the unregulated one. It also demonstrated that the stability gain by
negative feedback is preserved.

We looked at how stability of autoregulatory system gets affected on changing the values
of various parameters and can conclude that it decreases considerably when:
- Binding constant for the repressor is low
- Transcription rate is very low
- Repressor has a short half-life
Stability is not much affected by the value of binding constant of promoter.

The stability ratio(S<sub>r</sub> ) is >= 1 for all positive values of parameters and steady state
concentrations. Hence, we showed that the autoregulatory system is generally superior,
and only equal to the unregulated system under certain conditions. Those conditions
where both the systems converge can be found by detailed mathematical analysis.

## References
[1] Becskei, A., and L. Serrano. ”Engineering Stability in Gene Networks by Autoregu-
lation.” Nature 405 (2000): 590–3.<br/>
[2] Wolf, D. M. Eeckman, F. H. On the relationship between genomic regulatory element
organization and gene regulatory dynamics. J. Theor. Biol. 195, 167–186 (1998).<br/>
[3] Alon, U. An Introduction to Systems Biology: Design Principles of Biological Cir-
cuits. Chapman and Hall CRC, 2006 - Chapter 3.<br/>
[4] Strogatz, Steven H. Nonlinear Dynamics and Chaos: With Applications to Physics,
Biology, Chemistry, and Engineering. Westview Press, 2014 - Chapters 1 and 2.<br/>
[5] https://www.sciencedirect.com/topics/neuroscience/rna-polymerase<br/>
[6] https://www.sciencedirect.com/topics/neuroscience/repressor<br/>
[7] https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/regulation-of-gene-expression-and-cell-specialization/a/eukaryotic-transcription-factors<br/>
