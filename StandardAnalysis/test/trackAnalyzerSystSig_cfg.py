from OSUT3Analysis.AnaTools.osuAnalysis_cfi import *
from DisappTrks.StandardAnalysis.trackAnalyzerCondor_cfg import *
###############################################################
##### Set Options for Running your Analyzer Interactively #####
###############################################################
process.source.fileNames.append('file:/home/wulsin/disappTrks/analysisTemplateV3/CMSSW_6_1_2/src/DisappTrks/StandardAnalysis/test/condor/condor_2014_01_25_MetJetSkim/AMSB_mGrav75K_1ns/MetJet/bean_0.root')  
process.maxEvents.input = 200
#process.MessageLogger.cerr.FwkReport.reportEvery = 1


# For pile-up systematic:  
## process.OSUAnalysis.dataPU = cms.string ('PU_data_190456_208686_66805xSec')  # PU low xsec
process.OSUAnalysis.dataPU = cms.string ('PU_data_190456_208686_69300xSec')  # PU central value (STANDARD)
## process.OSUAnalysis.dataPU = cms.string ('PU_data_190456_208686_71795xSec')  # PU high xsec 

# For trigger efficiency systematic:  
process.OSUAnalysis.triggerMetSFFile = cms.string ('')    # no trigger eff correction (STANDARD)
#process.OSUAnalysis.triggerMetSFFile = cms.string (os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/data/TriggerMetSF.root')  # with trigger eff correction  

# For trigger efficiency systematic:  
process.OSUAnalysis.trackNMissOutSFFile = cms.string ('')    # no trigger eff correction  (STANDARD)  
#process.OSUAnalysis.trackNMissOutSFFile = cms.string (os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/data/NHitsMissingOuterSF_muonTagProbe.root')  # with track NMissOut correction  
#process.OSUAnalysis.trackNMissOutSFFile = cms.string (os.environ['CMSSW_BASE']+'/src/DisappTrks/StandardAnalysis/data/NHitsMissingOuterSF_elecTagProbe.root')  # with track NMissOut correction  

# For PDF systematic:  
process.OSUAnalysis.calcPdfWeights = cms.bool(False)    # no calculation of weights (STANDARD)  
#process.OSUAnalysis.calcPdfWeights = cms.bool(True)      # calculate weights 
process.OSUAnalysis.pdfSetFlag  = cms.int32(1)            # ignored if calcPdfWeights = False
process.OSUAnalysis.pdfSet  = cms.string('cteq66.LHgrid') # ignored if calcPdfWeights = False 
# Other PDF variations:
## process.OSUAnalysis.pdfSet  = cms.string('cteq6ll.LHpdf')  
## process.OSUAnalysis.pdfSet  = cms.string('CT10.LHgrid')  
## process.OSUAnalysis.pdfSet  = cms.string('cteq66alphas.LHgrid')  


# For JES and JERsystematic:
process.OSUAnalysis.flagJESJERCorr = cms.bool (False)    # no  correction  (STANDARD)
process.OSUAnalysis.jESJERCorr = cms.string ('')    # no correction  (STANDARD)

#process.OSUAnalysis.flagJESJERCorr = cms.bool(True)    
#process.OSUAnalysis.jESJERCorr = cms.string('JESup')    #with JES correction
#process.OSUAnalysis.jESJERCorr = cms.string('JESdown')  #with JES correction
#process.OSUAnalysis.jESJERCorr = cms.string('JERup')    #with JER correction
#process.OSUAnalysis.jESJERCorr = cms.string('JERdown')  #with JER correction


########################################################################
##### Import the information about all the histograms to be filled #####
########################################################################


##########################################################
##### Add the Desired Channels to the List to be Run #####
##########################################################
from DisappTrks.StandardAnalysis.MyEventSelections_disappTrks import *


################################
## Channels for Analysis Note ##
################################
process.OSUAnalysis.channels.append(FullSelection)

