#!/usr/bin/env python
# Plot of the distribution of isolation energy, comparing
# tracks matched to pions, electrons, and no match.  
input_histograms = [
    { 'dataset' : 'QCD_470to600_Reco',
      'channel' : 'PreSelectionPMissingElectronId', 
      'name' : 'caloTotDeltaRp5ByP',
      'legend_entry' : 'matched to electron',
      'color' : 2,
                },
    { 'dataset' : 'QCD_470to600_Reco',
      'channel' : 'PreSelectionPMissingPionId', 
      'name' : 'caloTotDeltaRp5ByP',
      'legend_entry' : 'matched to pion',
      'color' : 4,
                },
    { 'dataset' : 'QCD_470to600_Reco',
      'channel' : 'PreSelectionPMissingNotGenMatched',  
      'name' : 'caloTotDeltaRp5ByP',  
      'legend_entry' : 'not matched',
      'color' : 1,
                },
    ]



