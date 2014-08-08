import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.MyCuts_disappTrks import *  # Put all the individual cuts in this file 
################################################
##### List of cut VPSets                   #####
################################################


cutsStdClean = cms.VPSet (
    cutEvtFilter,
    cutVtxGood, 
    )

cutsMET = cms.VPSet (
    cutMET,
)

cutsJets = cms.VPSet (
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutMetDeltaPhiMin2Jets0p5, 
)


cutsJetsNoNoiseClean = cms.VPSet (
##     cutSecJetPt,
##     cutSecJetEta2p4,
##     cutJetPt30,
##     cutJetEta4p5,  # Not committed
##     cutJetJetDPhi,
    )


cutsJetsNoDPhi = cms.VPSet (
    cutSecJetPt,
    cutSecJetEta2p4,
    cutSecJetNoiseChgHad,
    cutSecJetNoiseChgEM,
    cutSecJetNoiseNeuHad,
    cutSecJetNoiseNeuEM,
    cutSubLeadingJetID,
    )


cutsTrkPtEta = cms.VPSet (
    cutTrkPt,
    cutTrkEta,
    )

cutsTrkQuality = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkNHits,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkQualityFiveHits = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkNHitsIs5,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkQualitySevenHits = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkNHitsIs7,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )


cutsTrkQualityNoNHits = cms.VPSet (
    cutTrkD0,
    cutTrkDZ,
    cutTrkHitMissMid,
    cutTrkHitMissIn,
    )

cutsTrkIso = cms.VPSet (
    cutTrkRelIsoRp3,  
    cutTrkJetDeltaR,
    )

cutsTrkVetoRegions = cms.VPSet (
    cutTrkCrackVeto,
    cutTrkWheel0GapVeto, 
    cutTrkEtaMuonPk, 
    cutTrkDeadEcalVeto,
    cutTrkEcalGap1,
    cutTrkEcalGap2,
    cutTrkEcalGap3,
    cutTrkEcalGap4,
    cutTrkEcalGap5,
    cutTrkEcalGap6,
    cutTrkEcalGap7,
    cutTrkBadCSCVeto, 
    )

cutsTrkLeptonVeto = cms.VPSet (
    cutTauLooseHadronicVeto,  
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto, 
    )

cutsTrkLeptonVetoNoMu = cms.VPSet (
    cutTauLooseHadronicVeto,
    cutElecLooseIDVeto,
    )


cutsTrkPreselFiveHits = \
  cutsTrkVetoRegions + \
  cutsTrkQualityFiveHits + \
  cutsTrkIso + \
  cutsTrkLeptonVeto

cutsTrkPreselSevenHits = \
                      cutsTrkVetoRegions + \
                      cutsTrkQualitySevenHits + \
                      cutsTrkIso + \
                      cutsTrkLeptonVeto



cutsTrkPresel = \
              cutsTrkPtEta + \
              cutsTrkVetoRegions + \
              cutsTrkQuality + \
              cutsTrkIso + \
              cutsTrkLeptonVeto

cutsTrkPreselNoLepVeto = \
  cutsTrkPtEta + \
  cutsTrkVetoRegions + \
  cutsTrkQuality + \
  cutsTrkIso

cutsTrkPreselNoLepVetoNoIso = \
                       cutsTrkPtEta + \
                       cutsTrkVetoRegions + \
                       cutsTrkQuality 


cutsTrkPreselNoLepVetoOrVetoRegion = \
  cutsTrkPtEta + \
  cutsTrkQuality + \
  cutsTrkIso


cutsTrkPreselNoMuCuts = \
  cutsTrkPtEta + \
  cms.VPSet(
    cutTrkCrackVeto,
    cutTrkDeadEcalVeto,
    ) + \
  cutsTrkQuality + \
  cutsTrkIso + \
  cutsTrkLeptonVeto 

cutsTrkPreselNoMuCutsNoLepVeto = \
  cutsTrkPtEta + \
  cms.VPSet(
    cutTrkCrackVeto,
    cutTrkDeadEcalVeto,
    ) + \
  cutsTrkQuality + \
  cutsTrkIso


cutsPresel = \
  cutsStdClean + \
  cutsMET + \
  cutsJets + \
  cutsTrkPresel

cutsPreselCtrlNMiss = copy.deepcopy(cutsPresel)
for cut in cutsPreselCtrlNMiss:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsPreselCtrlNMiss.append(cutTrkHitMissOutInv)

cutsTrkPreselCtrlNMiss = copy.deepcopy(cutsTrkPresel)
for cut in cutsTrkPreselCtrlNMiss:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsTrkPreselCtrlNMiss.append(cutTrkHitMissOutInv)  

cutsPreselCtrlEcalo = copy.deepcopy(cutsPresel)
for cut in cutsPreselCtrlEcalo:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsPreselCtrlEcalo.append(cutMaxCalo10Inv)  

cutsTrkPreselCtrlEcalo = copy.deepcopy(cutsTrkPresel)
for cut in cutsTrkPreselCtrlEcalo:  
    if cut.cutString == cutTrkPt.cutString:
        cut.cutString = cutTrkPt30.cutString # replace pT>50 with pT>30 cut  
cutsTrkPreselCtrlEcalo.append(cutMaxCalo10Inv)   


cutsPreselFiveHits = \
           cutsStdClean + \
           cutsMET + \
           cutsJets + \
           cutsTrkPreselFiveHits

cutsPreselSevenHits = \
                   cutsStdClean + \
                   cutsMET + \
                   cutsJets + \
                   cutsTrkPreselSevenHits

cutsPreselNoMet = \
  cutsJets + \
  cutsTrkPresel

cutsSigReg = cms.VPSet (
    cutMaxCalo10, 
    cutTrkHitMissOut,
    )

cutsFullSelection = \
  cutsPresel + \
  cutsSigReg

cutsTrkIdOther = cms.VPSet (
  cutTrkMuonIdInv, 
  cutTrkElecIdInv, 
  cutTrkTauIdInv, 
  cutTrkNotGenMatchedInv
  )

cutsTrkPreselSigReg = \
  cutsTrkPresel + \
  cms.VPSet (
    cutMaxCalo10, 
    cutTrkHitMissOut,
    )

cutsTagMuon = cms.VPSet (
    # See SMP-12-023 for example of W->mu nu selection  
    cutMuonPt25,
    cutMuonEta,
    cutMuonTightID,
    cutMuonPFIso,
    )

cutsTagElec = cms.VPSet (
    # See https://twiki.cern.ch/twiki/bin/view/CMS/MultivariateElectronIdentification#Triggering_MVA  
    cutElecPt20,
    cutElecEta,
    cutElecMva,
    cutElecPFIso,
    cutElecD0,
    cutElecDZ,
    cutElecPassConvVeto, 
    cutElecLostHits, 
    )


cutsMuTauHad = cms.VPSet (
    cutTauPt,
    cutTauEta,
    cutTauAgainstElectron,
    cutTauAgainstMuonTight,
    cutTauDecayModeFinding,
    cutTauLooseIso,
    cutMuonLooseIDOnlyOne,
    cutMuonEta,
    cutMuonPt25,
    cutMuonTightID,
    cutMuonPFIso,
    cutMuonD0,
    cutMuonDZ,
    cutMuonMetMT,
    )

cutsMuTrk = cms.VPSet (
#    cutTauPt,
#    cutTauEta,
#    cutTauAgainstElectron,
#    cutTauAgainstMuonTight,
#    cutTauDecayModeFinding,
#    cutTauLooseIso,
    cutMuonLooseIDOnlyOne,
    cutMuonEta,
    cutMuonPt25,
    cutMuonTightID,
    cutMuonPFIso,
    cutMuonD0,
    cutMuonDZ,
    cutMuonMetMT,
    )

cutsMuTauHadZPeak = cms.VPSet (
    cutMuTauCharge,
    cutMuTauInvMass,
#    cutMuTrkDeltaR,
#    cutTauTrkDeltaR,
    )

cutsMuTrkHadZPeak = cms.VPSet (
    cutMuTrkChgOpp,
    cutMuTrkInvMass,
    #    cutMuTrkDeltaR,
    #    cutTauTrkDeltaR,
    )

    
cutsMuTrkZPeak = cms.VPSet (
    cutMuTrkInvMass80To100,
    cutMuTrkChgOpp,
    )

cutsElecTrkZPeak = cms.VPSet (
    cutElecTrkInvMass80To100,
    cutElecTrkChgOpp,
    )


################################################
##### List of  event selections (channels) #####
################################################
SingleElecTrigTrkPreselNoElecVetoLowMet = cms.PSet( # Use for Monojet trigger efficiency
        name = cms.string("SingleElecTrigTrkPreselNoElecVetoLowMet"),
        triggers = triggersSingleElec,
        cuts =
        cutsStdClean +
        cms.VPSet(cutMaxMET200) + 
        cutsJets +
        cms.VPSet(
    cutSecJetLeadingPt,
    
    ) + cutsTrkPreselNoLepVeto
        + cms.VPSet(cutMuonLooseIDVeto,cutSecMuonLooseIDVeto,cutTauLooseHadronicVeto )
       # + cms.VPSet(cutMCPartPdgNuE, cutMCPartStatus3)
        )

SingleElecTrigNoElecVeto = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleElecTrigNoElecVeto"),
    triggers = triggersSingleElec,
    cuts =
    cutsStdClean +
#    cms.VPSet(cutMaxMET200) +
    cutsJets +
    cms.VPSet(
    cutSecJetLeadingPt,
    
    ) #+ cutsTrkPreselNoLepVeto
    + cms.VPSet(cutMuonLooseIDVeto,cutSecMuonLooseIDVeto,cutTauLooseHadronicVeto,)
    # + cms.VPSet(cutMCPartPdgNuE, cutMCPartStatus3)
    )


SingleElecTrigTrkPreselNoElecVetoHighMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("SingleElecTrigTrkPreselNoElecVetoHighMet"),
    triggers = triggersSingleElec,
    cuts =
    cutsStdClean +
    cms.VPSet(cutMET200) +
    cutsJets +
    cms.VPSet(
    cutSecJetLeadingPt,
    
    ) + cutsTrkPreselNoLepVeto
    + cms.VPSet(cutMuonLooseIDVeto,cutSecMuonLooseIDVeto,cutTauLooseHadronicVeto,)
    #    + cms.VPSet(cutMCPartPdgNuE, cutMCPartStatus3)
    #    + cms.VPSet(cutOldMuonLooseIDVeto,cutOldSecMuonLooseIDVeto,cutTauLooseHadronicVeto,)
    )




MonojetTrigTrkPreselNoElecVetoLowMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoElecVetoLowMet"),
    triggers = triggersJetMet95,
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoLowMet.cuts)
    )

MonojetTrigNoElecVeto = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigNoElecVeto"),
    triggers = triggersJetMet95,
    cuts = copy.deepcopy(SingleElecTrigNoElecVeto.cuts)
    )

MonojetTrigTrkPreselNoElecVetoHighMet = cms.PSet( # Use for Monojet trigger efficiency
    name = cms.string("MonojetTrigTrkPreselNoElecVetoHighMet"),
    triggers = triggersJetMet95,
    cuts = copy.deepcopy(SingleElecTrigTrkPreselNoElecVetoHighMet.cuts)
    )



TauBkgdMismeasure = cms.PSet(
    name = cms.string("TauBkgdMismeasure"),
    triggers = triggersJetMet,
    cuts =
#    cutsPreselFiveHits +
    cutsPreselSevenHits +
    cms.VPSet ( cutTrkEta  ) +
    cms.VPSet ( cutTrkHitMissOut  ) +
    cms.VPSet ( cutTrkTauId ) 
    )

TauBkgdPreselNoTau = cms.PSet(
    name = cms.string("TauBkgdPreselNoTau"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkPt30, cutTrkEta  ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutElecLooseIDVeto,
    #cutTauLooseHadronicVeto,
    ),
    )

TauBkgdPresel = cms.PSet(
    name = cms.string("TauBkgdPresel"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkPt30, cutTrkEta  ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutElecLooseIDVeto,
    cutTauLooseHadronicVeto,
    ),
    )

Trigger95 = cms.PSet(
    triggers = triggersJetMet95,
    name = cms.string("Trigger95"),
    cuts = cms.VPSet (
    cutNoCuts,
    ),
                )
Trigger105 = cms.PSet(
    triggers = triggersJetMet105,
    name = cms.string("Trigger105"),
    cuts = cms.VPSet (
    cutNoCuts,
    ),
    )
Trigger105Emulate = cms.PSet(
    triggers = triggersJetMet105,
    name = cms.string("Trigger105Emulate"),
    cuts = cms.VPSet (
   cutNoCuts,
    ),
    )

TestBothTriggers = cms.PSet(
            triggers = triggersJetMet95105,
        name = cms.string("TestBothTriggers"),
            cuts = cms.VPSet (
        cutNoCuts,
            ),
            )



NoCuts = cms.PSet(
    name = cms.string("NoCuts"),
    cuts = cms.VPSet (
       cutNoCuts,
       ),
    )

# Use for plotting the stop lifetime  
StopLifetime = cms.PSet(
    name = cms.string("StopLifetime"),
    cuts = cms.VPSet (
       cutNoCuts,
       cutMCPartStatus3Filter,
       cutMCPartSusyFilter, 
#       cutStopPt50, 
       cutStopEta2p5,
#       cutStopCtauNegative, 
#       cutStopDauIdNotPion, 
       ),
    )

NoCutsFilterMC = cms.PSet(
    name = cms.string("NoCutsFilterMC"),
    cuts = cms.VPSet (
       cutMCPartStatus3Filter,
       cutMCPartSusyFilter,
#       cutSecJetLeadingPt, 
#       cutSubLeadingJetIDFilter, 
#       cutSubLeadingJetID, 
       ),
    )

NoCutsFilterMCFilterJet = cms.PSet(
    name = cms.string("NoCutsFilterMCFilterJet"),
    cuts = cms.VPSet (
       cutMCPartStatus3Filter,
       cutMCPartSusyFilter,
       cutSecJetLeadingPt, 
       cutSubLeadingJetID, 
       ),
    )

NoCutsFilterMCCtauZero = cms.PSet(
    name = cms.string("NoCutsFilterMCCtauZero"),
    cuts = copy.deepcopy(NoCutsFilterMC.cuts) + 
    cms.VPSet (
       cutStopCtauZero,  
       ),
    )

NoCutsFilterMCCtauNonZero = cms.PSet(
    name = cms.string("NoCutsFilterMCCtauNonZero"),
    cuts = copy.deepcopy(NoCutsFilterMC.cuts) + 
    cms.VPSet (
       cutStopCtauNonZero,  
       ),
    )

NoCutsDecayInTrackerN2 = cms.PSet(
    name = cms.string("NoCutsDecayInTrackerN2"),
    cuts = copy.deepcopy(NoCutsFilterMC.cuts) + 
    cms.VPSet (
    ##     cutStopDecayLengthNonZeroN2,
    ##     cutStopDecayLengthTrackerN2
    cutStopDecayLengthZeroVeto, 
    cutStopDecayLengthOutsideTrackerVeto, 
    ),
    )


DebugCuts = cms.PSet(
    name = cms.string("DebugCuts"),
    cuts = cms.VPSet (
       cms.PSet(
          inputCollection = cms.string("jets"),
#          cutString = cms.string("isLeadingPtJet == 1"),
          cutString = cms.string("pt > 0"),
          numberRequired = cms.string(">= 0"),
          ),
       )
    )

TriggerJetMet = cms.PSet(
    name = cms.string("TriggerJetMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
    ),
    )

TriggerMet = cms.PSet(
    name = cms.string("TriggerMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         ),
    )

TriggerMetNoMu = cms.PSet(
    name = cms.string("TriggerMetNoMu"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMETNoMu,
         ),
    )

Trigger = cms.PSet(
    name = cms.string("Trigger"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
    cutNoCuts,
    ),
    )

SkimMet90 = cms.PSet(
    name = cms.string("SkimMet90"),
    cuts = cms.VPSet (
    cutMET90, 
    ),
    )


SingleMuTrigger = cms.PSet(
    name = cms.string("MuTrigger"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
      cutNoCuts,
      ),
    )


TriggerJetMetDebug = cms.PSet(
    name = cms.string("TriggerJetMetDebug"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

TriggerJetMetDebug2 = cms.PSet(
    name = cms.string("TriggerJetMetDebug2"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        cutElecLooseIDVeto,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

TriggerJetMetDebug3 = cms.PSet(
    name = cms.string("TriggerJetMetDebug3"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,  
        cutSecJetPt,  # cut on secondary jets collection so that BNTree includes all jets  
        cutMuonLooseIDVeto,  # cut on secondary jets collection so that BNTree includes all jets  
        ),
    )

FullSelection = cms.PSet(
    name = cms.string("FullSelection"),
    triggers = triggersJetMet,
    cuts = cutsFullSelection, 
    )

FullSelectionMetJet95 = cms.PSet(
    name = cms.string("FullSelection"),
    triggers = triggersJetMet95Met120,
    #    triggers = triggersJetMet,
    cuts = cutsFullSelection,
    )

FullSelectionMetJet105 = cms.PSet(
    name = cms.string("FullSelection"),
    triggers = triggersJetMet105Met120,
    #    triggers = triggersJetMet,
    cuts = cutsFullSelection,
    )

FullSelectionReorder = copy.deepcopy(FullSelection)  
FullSelectionReorder.name = cms.string("FullSelectionReorder")
# First find the position of the new index
idx = -1
for i in range(len(FullSelectionReorder.cuts) - 1, -1, -1):
    if FullSelectionReorder.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        idx = i
for i in range(len(FullSelectionReorder.cuts) - 1, -1, -1):
    for j in range(0, len(cutsTrkVetoRegions)):
        if FullSelectionReorder.cuts[i].cutString == cutsTrkVetoRegions[j].cutString: 
            FullSelectionReorder.cuts.insert(idx-1, FullSelectionReorder.cuts.pop(i)) 


FullSelectionTrigEmulate95MC = copy.deepcopy(FullSelection)
FullSelectionTrigEmulate95MC.name = cms.string("FullSelectionTrigEmulate95MC")
FullSelectionTrigEmulate95MC.triggers = cms.string("")
FullSelectionTrigEmulate95MC.cuts.append(cutTriggerEmulateMonojet95MC)

FullSelectionTrigEmulate95data = copy.deepcopy(FullSelection)
FullSelectionTrigEmulate95data.name = cms.string("FullSelectionTrigEmulate95data")
FullSelectionTrigEmulate95data.triggers = cms.string("")
FullSelectionTrigEmulate95data.cuts.append(cutTriggerEmulateMonojet95data)

FullSelectionTrigEmulate105MC = copy.deepcopy(FullSelection)
FullSelectionTrigEmulate105MC.name = cms.string("FullSelectionTrigEmulate105MC")
FullSelectionTrigEmulate105MC.triggers = cms.string("")
FullSelectionTrigEmulate105MC.cuts.append(cutTriggerEmulateMonojet105MC)

FullSelectionTrigEmulate105data = copy.deepcopy(FullSelection)
FullSelectionTrigEmulate105data.name = cms.string("FullSelectionTrigEmulate105data")
FullSelectionTrigEmulate105data.triggers = cms.string("")
FullSelectionTrigEmulate105data.cuts.append(cutTriggerEmulateMonojet105data)


FullSelectionFilterMC = copy.deepcopy(FullSelection)
FullSelectionFilterMC.name = cms.string("FullSelectionFilterMC")
FullSelectionFilterMC.cuts.append(cutMCPartStatus3Filter)
FullSelectionFilterMC.cuts.append(cutMCPartSusyFilter)

FullSelectionFilterMCTrack = copy.deepcopy(FullSelectionFilterMC)
FullSelectionFilterMCTrack.name = cms.string("FullSelectionFilterMCTrack")
FullSelectionFilterMCTrack.cuts.append(cutTrkMCPartMatch)  

NoCutsFilterMCTrack = copy.deepcopy(NoCutsFilterMC)
NoCutsFilterMCTrack.name = cms.string("NoCutsFilterMCTrack")
NoCutsFilterMCTrack.cuts.append(cutTrkMCPartMatchFilter)  




FullSelectionDeadEcalLast = copy.deepcopy(FullSelection) 
FullSelectionDeadEcalLast.name = cms.string("FullSelectionDeadEcalLast") 
for i in xrange(len(FullSelectionDeadEcalLast.cuts) - 1, -1, -1):
    if FullSelectionDeadEcalLast.cuts[i].cutString == cutTrkDeadEcalVeto.cutString:
        del FullSelectionDeadEcalLast.cuts[i]
FullSelectionDeadEcalLast.cuts.append(cutTrkDeadEcalVeto)  
                

FullSelectionStopCtauZero = copy.deepcopy(FullSelection) 
FullSelectionStopCtauZero.name = cms.string("FullSelectionStopCtauZero") 
FullSelectionStopCtauZero.cuts.append(cutStopCtauZero)  

FullSelectionStopCtauNonZero = copy.deepcopy(FullSelection) 
FullSelectionStopCtauNonZero.name = cms.string("FullSelectionStopCtauNonZero") 
FullSelectionStopCtauNonZero.cuts.append(cutStopCtauNonZero)  



FullSelectionMet80Trig = cms.PSet(
    name = cms.string("FullSelectionMet80Trig"),
    triggers = triggersMet80,
    cuts = cutsFullSelection, 
    )

FullSelectionNoPt = cms.PSet(
    name = cms.string("FullSelectionNoPt"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
# remove the cuts after and including the trkRelIso cut
for i in xrange(len(FullSelectionNoPt.cuts) - 1, -1, -1):
    if FullSelectionNoPt.cuts[i].cutString == cutTrkPt.cutString:
        del FullSelectionNoPt.cuts[i]  

FullSelectionMCSig = cms.PSet(
    name = cms.string("FullSelectionMCSig"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
FullSelectionMCSig.cuts.append(cutMCPartStatus3)
FullSelectionMCSig.cuts.append(cutMCPartSusy)  


FullSelectionNoEta = cms.PSet(
    name = cms.string("FullSelectionNoEta"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoEta.cuts) - 1, 8, -1):
    if str(FullSelectionNoEta.cuts[i].cutString).find("eta") != -1:  
        del FullSelectionNoEta.cuts[i]  

FullSelectionNoBadCSC = cms.PSet(
    name = cms.string("FullSelectionNoBadCSC"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoBadCSC.cuts) - 1, -1, -1):
    if FullSelectionNoBadCSC.cuts[i].cutString == cutTrkBadCSCVeto.cutString:
        del FullSelectionNoBadCSC.cuts[i]  

FullSelectionNoD0 = cms.PSet(
    name = cms.string("FullSelectionNoD0"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoD0.cuts) - 1, -1, -1):
    if FullSelectionNoD0.cuts[i].cutString == cutTrkD0.cutString:
        del FullSelectionNoD0.cuts[i]  

FullSelectionNoDZ = cms.PSet(
    name = cms.string("FullSelectionNoDZ"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoDZ.cuts) - 1, -1, -1):
    if FullSelectionNoDZ.cuts[i].cutString == cutTrkDZ.cutString:
        del FullSelectionNoDZ.cuts[i]  

FullSelectionNoNhits = cms.PSet(
    name = cms.string("FullSelectionNoNhits"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoNhits.cuts) - 1, -1, -1):
    if FullSelectionNoNhits.cuts[i].cutString == cutTrkNHits.cutString:
        del FullSelectionNoNhits.cuts[i]  

FullSelectionNoRelIso = cms.PSet(
    name = cms.string("FullSelectionNoRelIso"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoRelIso.cuts) - 1, -1, -1):
    if FullSelectionNoRelIso.cuts[i].cutString == cutTrkRelIsoRp3.cutString or FullSelectionNoRelIso.cuts[i].cutString == cutTrkJetDeltaR.cutString: 
        del FullSelectionNoRelIso.cuts[i]  

FullSelectionNoCalo = cms.PSet(
    name = cms.string("FullSelectionNoCalo"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoCalo.cuts) - 1, -1, -1):
    if FullSelectionNoCalo.cuts[i].cutString == cutMaxCalo10.cutString:
        del FullSelectionNoCalo.cuts[i]  

FullSelectionNoMissHit = cms.PSet(
    name = cms.string("FullSelectionNoMissHit"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionNoMissHit.cuts) - 1, -1, -1):
    if FullSelectionNoMissHit.cuts[i].cutString == cutTrkHitMissOut.cutString:
        del FullSelectionNoMissHit.cuts[i]  



FullTrkSelection = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelection"),
    cuts = cutsTrkPreselSigReg, 
    )

FullTrkSelectionWTrig = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("FullTrkSelectionWTrig"),
    cuts = cutsTrkPreselSigReg, 
    )

FullTrkSelectionUpToMissIn = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionUpToMissIn"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
# remove the cuts after and including the trkRelIso cut
for i in range(0, len(FullTrkSelectionUpToMissIn.cuts)):  
    if FullTrkSelectionUpToMissIn.cuts[i].cutString == cutTrkRelIsoRp3.cutString:
        idx = i
del FullTrkSelectionUpToMissIn.cuts[idx:len(FullTrkSelectionUpToMissIn.cuts)]  

FullTrkSelectionUpToElecVeto = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionUpToElecVeto"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
# remove the cuts after and including the muon veto  
for i in range(0, len(FullTrkSelectionUpToElecVeto.cuts)):  
    if FullTrkSelectionUpToElecVeto.cuts[i].cutString == cutMuonLooseIDVeto.cutString:
        idx = i
del FullTrkSelectionUpToElecVeto.cuts[idx:len(FullTrkSelectionUpToElecVeto.cuts)]  

FullTrkSelectionUpToElecVetoWTrig = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("FullTrkSelectionUpToElecVetoWTrig"),
    cuts = copy.deepcopy(FullTrkSelectionUpToElecVeto.cuts), 
    )

FullTrkSelectionUpToMuonVeto = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionUpToMuonVeto"),
    cuts = copy.deepcopy(cutsTrkPresel), 
    )
# remove the elec veto 
for i in xrange(len(FullTrkSelectionUpToMuonVeto.cuts) - 1, -1, -1): 
    if FullTrkSelectionUpToMuonVeto.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del FullTrkSelectionUpToMuonVeto.cuts[i]

FullTrkSelectionUpToMuonVetoWTrig = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("FullTrkSelectionUpToMuonVetoWTrig"),
    cuts = copy.deepcopy(FullTrkSelectionUpToMuonVeto.cuts), 
    )

FullTrkSelectionLeadingJet = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionLeadingJet"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
FullTrkSelectionLeadingJet.cuts.append(cutJetLeadingPt)  

FullTrkSelectionJetPt = cms.PSet(
    # No cuts on Met or jet or trigger
    name = cms.string("FullTrkSelectionJetPt"),
    cuts = copy.deepcopy(cutsTrkPreselSigReg), 
    )
FullTrkSelectionJetPt.cuts.append(cutJetPt)  


MetJet = cms.PSet(
    name = cms.string("MetJet"),
    triggers = triggersJetMet,
    cuts =
    cutsStdClean + 
    cutsMET +
    cutsJets, 
    )

MetJetTrig105 = cms.PSet(
    name = cms.string("MetJetTrig105"),
    triggers = triggersJetMet105Met120,
    cuts =
    cutsMET +
    cutsJets,
    )

PreSelection = cms.PSet(
    name = cms.string("PreSelection"),
    triggers = triggersJetMet,
    cuts = cutsPresel, 
    )




ModelIndepGen = cms.PSet(
    name = cms.string("ModelIndepGen"),
    cuts = cms.VPSet(
    cutMCPartStatus3,
    cutMCPartSusy,
    cutMCPartChiPlus, # only consider the positive particles, so that there is a single candidate particle per event  
    cutMCPartEta2p2,
    cutMCPartPt50,
    cutStopDecayLengthTrackerXY,
    cutStopDecayLengthTrackerZ,
    cutStopMCPartMatch,
    ), 
    )

ModelIndepGenTest = cms.PSet(
    name = cms.string("ModelIndepGenTest"),
    cuts = cms.VPSet(
    cutMCPartStatus3,
#    cutMCPartSusy,
    cutMCPartChiPlus, # only consider the positive particles, so that there is a single candidate particle per event  
##     cutMCPartEta2p2,
##     cutMCPartPt50,
    cutStopDecayLengthTrackerXY,
#    cutStopDecayLengthTrackerZ,
    ), 
    )

ModelIndepMetJet = copy.deepcopy(ModelIndepGen) 
ModelIndepMetJet.name = cms.string("ModelIndepMetJet") 
ModelIndepMetJet.triggers = triggersJetMet105Met120 
ModelIndepMetJet.cuts = ModelIndepMetJet.cuts + \
                        MetJet.cuts
for i in xrange(len(ModelIndepMetJet.cuts) - 1, -1, -1):
    if ModelIndepMetJet.cuts[i].cutString == cutStopMCPartMatch.cutString:
        ModelIndepMetJet.cuts.insert(len(ModelIndepMetJet.cuts), ModelIndepMetJet.cuts.pop(i))
        # move cutStopMCPartMatch to the end of cutflow, to avoid problem identified in slides 20140724_groupMtg, p. 24.  

ModelIndepFullSel = copy.deepcopy(ModelIndepGen) 
ModelIndepFullSel.name = cms.string("ModelIndepFullSel") 
ModelIndepFullSel.triggers = triggersJetMet105Met120 
ModelIndepFullSel.cuts = ModelIndepFullSel.cuts + \
                         FullSelection.cuts + \
                         cms.VPSet(cutTrkMCPartMatch)
for i in xrange(len(ModelIndepFullSel.cuts) - 1, -1, -1):
    if ModelIndepFullSel.cuts[i].cutString == cutStopMCPartMatch.cutString:
        ModelIndepFullSel.cuts.insert(len(ModelIndepFullSel.cuts), ModelIndepFullSel.cuts.pop(i))
        # move cutStopMCPartMatch to the end of cutflow, to avoid problem identified in slides 20140724_groupMtg, p. 24.  


PreSelectionElecIdNoLepVeto = cms.PSet(
    name = cms.string("PreSelectionElecIdNoElecVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPtEta +
    cutsTrkQuality +
    cutsTrkIso +
    cms.VPSet ( cutTrkWheel0GapVeto ) +
    cms.VPSet ( cutTrkEtaMuonPk ) +
    cms.VPSet ( cutTrkBadCSCVeto ) +
    cms.VPSet ( cutTrkElectronId ) +
    cutsSigReg
    
    )

PreSelectionNoLepVeto = cms.PSet(
    name = cms.string("PreSelectionNoLepVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsTrkPreselNoLepVeto
    )


FullSelectionNoMet = copy.deepcopy(FullSelection)
FullSelectionNoMet.name = cms.string("FullSelectionNoMet")
for i in xrange(len(FullSelectionNoMet.cuts) - 1, -1, -1):
    if FullSelectionNoMet.cuts[i].cutString == cutMET.cutString:
        del FullSelectionNoMet.cuts[i]

PreSelectionNoMet = copy.deepcopy(PreSelection)
PreSelectionNoMet.name = cms.string("PreSelectionNoMet")
for i in xrange(len(PreSelectionNoMet.cuts) - 1, -1, -1):
    if PreSelectionNoMet.cuts[i].cutString == cutMET.cutString:
        del PreSelectionNoMet.cuts[i]


FullSelectionNoMetLeadJetMonojet95 = cms.PSet(
    name = cms.string("FullSelectionNoMetLeadJetMonojet95"),
    triggers = triggersJetMet95Met120,
    cuts =
    cutsJets +
    cms.VPSet ( cutSecJetLeadingPt ) +
#    cutsTrkPresel +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionNoMetLeadJetMonojet105 = cms.PSet(
        name = cms.string("FullSelectionNoMetLeadJetMonojet105"),
            triggers = triggersJetMet105Met120,
            cuts =
            cutsJets +
            cms.VPSet ( cutSecJetLeadingPt ) +
        #    cutsTrkPresel +
            cutsTrkPresel +
            cutsSigReg
            )

FullSelectionNoMetLeadJetBoth = cms.PSet(
        name = cms.string("FullSelectionNoMetLeadJetBoth"),
            triggers = triggersJetMet,
            cuts =
            cutsJets +
            cms.VPSet ( cutSecJetLeadingPt) +
        #    cutsTrkPresel +
            cutsTrkPresel +
            cutsSigReg
            )

FullSelectionNoMetLeadJetEmulate = cms.PSet(
            name = cms.string("FullSelectionNoMetLeadJetEmulate"),
#                        triggers = triggersJetMet,
                        cuts =
            cms.VPSet ( cutHlt105) +
                        cutsJets +
                        cms.VPSet ( cutSecJetLeadingPt) +
                    #    cutsTrkPresel +
                        cutsTrkPresel +
                        cutsSigReg
                        )


FullSelectionNoMetLeadJetChi = cms.PSet(
    name = cms.string("FullSelectionNoMetLeadJetChi"),
    triggers = triggersJetMet95,
    cuts =
    cutsJets +
    cms.VPSet ( cutSecJetLeadingPt,cutOldMuonLooseIDVeto,cutOldSecMuonLooseIDVeto, cutMCPartChi) +
    #    cutsTrkPresel +
    cutsTrkPresel +
    cutsSigReg
    )


FullSelectionNoMetLeadJetMet = cms.PSet(
    name = cms.string("FullSelectionNoMetLeadJetMet"),
    triggers = triggersMet120,
    cuts =
    cutsJets +
    cms.VPSet ( cutSecJetLeadingPt) +
    #    cutsTrkPresel +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionHighMet = cms.PSet(
    name = cms.string("FullSelectionHighMet"),
    triggers = triggersJetMet95,
    cuts =
    cms.VPSet(cutMET200) + 
    cutsJets +
    cms.VPSet ( cutSecJetLeadingPt ) +
    #    cutsTrkPresel +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionLowMet = cms.PSet(
    name = cms.string("FullSelectionLowMet"),
    triggers = triggersJetMet95,
    cuts =
    cms.VPSet(cutMaxMET200) +
    cutsJets +
    cms.VPSet ( cutSecJetLeadingPt ) +
    #    cutsTrkPresel +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionLowMetNoTrig = cms.PSet(
    name = cms.string("FullSelectionLowMetNoTrig"),
    cuts =
    cms.VPSet(cutMaxMET200) +
    cutsJets +
    cms.VPSet ( cutSecJetLeadingPt ) +
    #    cutsTrkPresel +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionNoMetJet150 = cms.PSet(
    name = cms.string("FullSelectionNoMetJet150"),
    triggers = triggersJetMet,
    cuts =
    cutsJets +
    cms.VPSet(cutJetPt150, cutSecJetPt150) +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionNoMetNoTrigJet150 = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrigJet150"),
    #triggers = triggersJetMet,
    cuts =
    cutsJets +
    cms.VPSet(cutJetPt150, cutSecJetPt150) +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionNoMetNoTrigLeadJet = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrigLeadJet"),
    #triggers = triggersJetMet,
    cuts =
    cutsJets +
    cms.VPSet(cutSecJetLeadingPt) +
    cutsTrkPresel +
    cutsSigReg
    )

FullSelectionNoMetNoTrigLeadJetChi = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrigLeadJetChi"),
    #triggers = triggersJetMet,
    cuts =
    cutsJets +
    cms.VPSet(cutSecJetLeadingPt,cutOldMuonLooseIDVeto,cutOldSecMuonLooseIDVeto, cutMCPartChi) +
    cutsTrkPresel +
    cutsSigReg
    )



FullSelectionNoMetNoTrig = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrig"),
    cuts = copy.deepcopy(FullSelectionNoMet.cuts), 
    )


FullSelectionFakeTrk = cms.PSet(
    name = cms.string("FullSelectionFakeTrk"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
idx = len(cutsMET) + len(cutsJets)  
FullSelectionFakeTrk.cuts.insert(idx, cutTrkNotGenMatched) 


FullSelectionNoTrkCuts = cms.PSet(
    name = cms.string("FullSelectionNoTrkCuts"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets 
    )

FullSelectionNoMetFakeTrk = cms.PSet(
    name = cms.string("FullSelectionNoMetFakeTrk"),
    triggers = triggersJetMet,
    cuts = 
    cutsJets + 
    cms.VPSet ( cutTrkNotGenMatched ) + 
    cutsTrkPresel + 
    cutsSigReg
    )

FullSelectionNoMetNoTrkCuts = cms.PSet(
    name = cms.string("FullSelectionNoMetNoTrkCuts"),
    triggers = triggersJetMet,
    cuts = 
    cutsJets 
    )


PreSelectionNoNoiseClean = cms.PSet(
    name = cms.string("PreSelectionNoNoiseClean"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJetsNoNoiseClean 
    )

MetJetSelNoJetJetDPhi = cms.PSet(
    name = cms.string("MetJetSelNoJetJetDPhi"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJetsNoDPhi 
    )

PreSelectionNoJetJetDPhi_NoMetDPhi = copy.deepcopy(PreSelection)
PreSelectionNoJetJetDPhi_NoMetDPhi.name = cms.string("PreSelectionNoJetJetDPhi_NoMetDPhi")
for i in xrange(len(PreSelectionNoJetJetDPhi_NoMetDPhi.cuts) - 1, -1, -1):
    if PreSelectionNoJetJetDPhi_NoMetDPhi.cuts[i].cutString == cutMetDeltaPhiMin2Jets0p5.cutString or \
       PreSelectionNoJetJetDPhi_NoMetDPhi.cuts[i].cutString == cutJetJetDPhi.cutString:
        del PreSelectionNoJetJetDPhi_NoMetDPhi.cuts[i] 

PreSelectionNoMetDPhi = copy.deepcopy(PreSelection)
PreSelectionNoMetDPhi.name = cms.string("PreSelectionNoMetDPhi")
for i in xrange(len(PreSelectionNoMetDPhi.cuts) - 1, -1, -1):
    if PreSelectionNoMetDPhi.cuts[i].cutString == cutMetDeltaPhiMin2Jets0p5.cutString:
        del PreSelectionNoMetDPhi.cuts[i] 

PreSelectionNoJetJetDPhi = copy.deepcopy(PreSelection)
PreSelectionNoJetJetDPhi.name = cms.string("PreSelectionNoJetJetDPhi")
for i in xrange(len(PreSelectionNoJetJetDPhi.cuts) - 1, -1, -1):
    if PreSelectionNoJetJetDPhi.cuts[i].cutString == cutJetJetDPhi.cutString:
        del PreSelectionNoJetJetDPhi.cuts[i] 

PreSelectionNoPt = copy.deepcopy(PreSelection)
PreSelectionNoPt.name = cms.string("PreSelectionNoPt")
for i in xrange(len(PreSelectionNoPt.cuts) - 1, -1, -1):
    if PreSelectionNoPt.cuts[i].cutString == cutTrkPt.cutString:
        del PreSelectionNoPt.cuts[i] 

PreSelectionNoJet = copy.deepcopy(PreSelection)
PreSelectionNoJet.name = cms.string("PreSelectionNoJet")
for i in xrange(len(PreSelectionNoJet.cuts) - 1, -1, -1):
    if PreSelectionNoJet.cuts[i].cutString == cutSecJetPt.cutString:
        del PreSelectionNoJet.cuts[i] 

PreSelectionNoJet_LeadingJetFilter = copy.deepcopy(PreSelectionNoJet)
PreSelectionNoJet_LeadingJetFilter.name = cms.string("PreSelectionNoJet_LeadingJetFilter")
PreSelectionNoJet_LeadingJetFilter.cuts.append(cutSecJetLeadingPt)

PreSelectionNoNHit = copy.deepcopy(PreSelection)
PreSelectionNoNHit.name = cms.string("PreSelectionNoNHit")
for i in xrange(len(PreSelectionNoNHit.cuts) - 1, -1, -1):
    if PreSelectionNoNHit.cuts[i].cutString == cutTrkNHits.cutString:
        del PreSelectionNoNHit.cuts[i] 


PreSelectionNoIso = cms.PSet(
    name = cms.string("PreSelectionNoIso"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPtEta +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    cutsTrkLeptonVeto
    )

PreSelectionNoTrkJetDR = copy.deepcopy(PreSelection)
PreSelectionNoTrkJetDR.name = cms.string("PreSelectionNoTrkJetDR")  
for i in xrange(len(PreSelectionNoTrkJetDR.cuts) - 1, -1, -1):
    if PreSelectionNoTrkJetDR.cuts[i].cutString == cutTrkJetDeltaR.cutString:
        del PreSelectionNoTrkJetDR.cuts[i]

PreSelectionNoRelIsoRp3 = copy.deepcopy(PreSelection)
PreSelectionNoRelIsoRp3.name = cms.string("PreSelectionNoRelIsoRp3")  
for i in xrange(len(PreSelectionNoRelIsoRp3.cuts) - 1, -1, -1):
    if PreSelectionNoRelIsoRp3.cuts[i].cutString == cutTrkRelIsoRp3.cutString:
        del PreSelectionNoRelIsoRp3.cuts[i] 

PreSelectionNoMissIn = copy.deepcopy(PreSelection)
PreSelectionNoMissIn.name = cms.string("PreSelectionNoMissIn")  
for i in xrange(len(PreSelectionNoMissIn.cuts) - 1, -1, -1):
    if PreSelectionNoMissIn.cuts[i].cutString == cutTrkHitMissIn.cutString:
        del PreSelectionNoMissIn.cuts[i] 

PreSelectionNoMissMid = copy.deepcopy(PreSelection)
PreSelectionNoMissMid.name = cms.string("PreSelectionNoMissMid")  
for i in xrange(len(PreSelectionNoMissMid.cuts) - 1, -1, -1):
    if PreSelectionNoMissMid.cuts[i].cutString == cutTrkHitMissMid.cutString:
        del PreSelectionNoMissMid.cuts[i] 

PreSelectionNoMuonFiducial = copy.deepcopy(PreSelection)
PreSelectionNoMuonFiducial.name = cms.string("PreSelectionNoMuonFiducial")  
for i in xrange(len(PreSelectionNoMuonFiducial.cuts) - 1, -1, -1):
    if PreSelectionNoMuonFiducial.cuts[i].cutString == cutTrkWheel0GapVeto.cutString or \
       PreSelectionNoMuonFiducial.cuts[i].cutString == cutTrkEtaMuonPk.cutString or \
       PreSelectionNoMuonFiducial.cuts[i].cutString == cutTrkBadCSCVeto.cutString:  
        del PreSelectionNoMuonFiducial.cuts[i] 

FullSelectionNoMuonFiducial = copy.deepcopy(FullSelection)
FullSelectionNoMuonFiducial.name = cms.string("FullSelectionNoMuonFiducial")  
for i in xrange(len(FullSelectionNoMuonFiducial.cuts) - 1, -1, -1):
    if FullSelectionNoMuonFiducial.cuts[i].cutString == cutTrkWheel0GapVeto.cutString or \
       FullSelectionNoMuonFiducial.cuts[i].cutString == cutTrkEtaMuonPk.cutString or \
       FullSelectionNoMuonFiducial.cuts[i].cutString == cutTrkBadCSCVeto.cutString:  
        del FullSelectionNoMuonFiducial.cuts[i] 


FullSelectionElecPreveto = cms.PSet(
    name = cms.string("FullSelectionElecPreveto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection),
    )
for i in xrange(len(FullSelectionElecPreveto.cuts) - 1, -1, -1):
    cut = FullSelectionElecPreveto.cuts[i]
    if cut.cutString == cutElecLooseIDVeto.cutString or cut.cutString == cutMaxCalo10.cutString: # remove elec veto and Ecalo cut
        del FullSelectionElecPreveto.cuts[i]

FullSelectionElecPrevetoKeepEcalo = copy.deepcopy(FullSelectionElecPreveto)
FullSelectionElecPrevetoKeepEcalo.name = cms.string("FullSelectionElecPrevetoKeepEcalo")
FullSelectionElecPrevetoKeepEcalo.cuts.append(cutMaxCalo10)  
        

FullSelectionTauPreveto = cms.PSet(
    name = cms.string("FullSelectionTauPreveto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionTauPreveto.cuts) - 1, -1, -1):
    cut = FullSelectionTauPreveto.cuts[i]
    if cut.cutString == cutTauLooseHadronicVeto.cutString or cut.cutString == cutMaxCalo10.cutString: # remove tau veto and Ecalo cut
        del FullSelectionTauPreveto.cuts[i]

FullSelectionMuPreveto = cms.PSet(
    name = cms.string("FullSelectionMuPreveto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionMuPreveto.cuts) - 1, -1, -1):
    cut = FullSelectionMuPreveto.cuts[i]
    if cut.cutString == cutMuonLooseIDVeto.cutString or cut.cutString == cutSecMuonLooseIDVeto.cutString: # remove muon veto 
        del FullSelectionMuPreveto.cuts[i]

FullSelectionMuPrevetoMetNoMu = cms.PSet(
    name = cms.string("FullSelectionMuPrevetoMetNoMu"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsFullSelection), 
    )
for i in xrange(len(FullSelectionMuPrevetoMetNoMu.cuts) - 1, -1, -1):
    cut = FullSelectionMuPrevetoMetNoMu.cuts[i]
    if cut.cutString == cutMET.cutString:
        cut.cutString = cutMETNoMu.cutString  # replace cutMET with cutMETNoMu
    if cut.cutString == cutMuonLooseIDVeto.cutString or cut.cutString == cutSecMuonLooseIDVeto.cutString: # remove muon veto 
        del FullSelectionMuPrevetoMetNoMu.cuts[i]

FullSelectionNHits4 = cms.PSet(
    name = cms.string("FullSelectionNHits4"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(FullSelection.cuts),
    )
for i in xrange(len(FullSelectionNHits4.cuts) - 1, -1, -1):
    if FullSelectionNHits4.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits4.cuts[i].cutString = cutTrkNHitsIs4.cutString
                
FullSelectionNHits4MinFake = cms.PSet(
    name = cms.string("FullSelectionNHits4MinFake"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(FullSelection.cuts),
    )
for i in xrange(len(FullSelectionNHits4MinFake.cuts) - 1, -1, -1):
    if FullSelectionNHits4MinFake.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits4MinFake.cuts[i].cutString = cutTrkNHits4Min.cutString
FullSelectionNHits4MinFake.cuts.append(cutTrkNotGenMatched)  

FullSelectionNHits3Min = copy.deepcopy(FullSelection)  
FullSelectionNHits3Min.name = cms.string("FullSelectionNHits3Min") 
for i in xrange(len(FullSelectionNHits3Min.cuts) - 1, -1, -1):
    if FullSelectionNHits3Min.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits3Min.cuts[i].cutString = cutTrkNHits3Min.cutString

FullSelectionNHits3 = copy.deepcopy(FullSelection)  
FullSelectionNHits3.name = cms.string("FullSelectionNHits3") 
for i in xrange(len(FullSelectionNHits3.cuts) - 1, -1, -1):
    if FullSelectionNHits3.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits3.cuts[i].cutString = cutTrkNHitsIs3.cutString

FullSelectionNHits5 = copy.deepcopy(FullSelection)  
FullSelectionNHits5.name = cms.string("FullSelectionNHits5") 
for i in xrange(len(FullSelectionNHits5.cuts) - 1, -1, -1):
    if FullSelectionNHits5.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits5.cuts[i].cutString = cutTrkNHitsIs5.cutString

FullSelectionNHits6 = copy.deepcopy(FullSelection)  
FullSelectionNHits6.name = cms.string("FullSelectionNHits6") 
for i in xrange(len(FullSelectionNHits6.cuts) - 1, -1, -1):
    if FullSelectionNHits6.cuts[i].cutString == cutTrkNHits.cutString:
        FullSelectionNHits6.cuts[i].cutString = cutTrkNHitsIs6.cutString


forDeadEcal = cms.PSet(
    name = cms.string("forDeadEcal"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkElectronId ) +
    cutsTrkPreselNoLepVetoOrVetoRegion +
    cms.VPSet ( cutMuonLooseIDVeto, cutSecMuonLooseIDVeto,  cutTauLooseHadronicVeto, cutTrkCrackVeto  ) +
    cms.VPSet (cutTrkHitMissOut)
    )

forDeadEcal_v2 = cms.PSet(
    name = cms.string("forDeadEcal_v2"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cms.VPSet ( cutTrkElectronId ) +
    cutsTrkPreselNoLepVetoOrVetoRegion +
    cms.VPSet ( cutMuonLooseIDVeto, cutSecMuonLooseIDVeto,  cutTauLooseHadronicVeto  ) +
    cms.VPSet (cutTrkHitMissOut) 
    )
        
        


StudyMuVeto = cms.PSet(
    name = cms.string("StudyMuVeto"),
#    triggers = triggersJetMet,
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
##         cutTrkMuonId,
##         cutMuonLooseIDVeto,
##         cutMET, 
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

StudyMuVeto2 = cms.PSet(
    name = cms.string("StudyMuVeto2"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutMET, 
        ),
    )

PreSelInvMuonVeto = cms.PSet(
    name = cms.string("PreSelInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto, 
      cutMuonLooseIDVetoInv
      ), 
    )

PreSelNoTauVeto = cms.PSet(
    name = cms.string("PreSelNoTauVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutElecLooseIDVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto
      ), 
    )
PreSelNoElecVeto = cms.PSet(
    name = cms.string("PreSelNoElecVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutTauLooseHadronicVeto,
    ),
    )

PreSelElecVeto = cms.PSet(
    name = cms.string("PreSelElecVeto"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutTauLooseHadronicVeto,
    ),
    )

PreSelElecId = cms.PSet(
    name = cms.string("PreSelElecId"),
    triggers = triggersJetMet,
    cuts =
    cutsMET +
    cutsJets +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutTauLooseHadronicVeto,
    cutTrkElectronId,
    ),
    )

PreSelNoLepVeto = cms.PSet(
    name = cms.string("PreSelNoLepVeto"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto, 
    )

PreSelInvElecVeto = cms.PSet(
    name = cms.string("PreSelectionInvElecVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
for cut in PreSelInvElecVeto.cuts:
    if cut.cutString == cutElecLooseIDVeto.cutString:
        cut.cutString = cutElecLooseIDVetoInv.cutString


PreSelInvTauVeto = cms.PSet(
    name = cms.string("PreSelectionInvTauVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
for cut in PreSelInvTauVeto.cuts:
    if cut.cutString == cutTauLooseHadronicVeto.cutString:
        cut.cutString = cutTauLooseHadronicVetoInv.cutString


PreSelElecVetoEnd = cms.PSet(
    name = cms.string("PreSelElecVetoEnd"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto, 
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto, 
      cutElecLooseIDVeto,
      ), 
    )

PreSelMuonVetoEnd = cms.PSet(
    name = cms.string("PreSelMuonVetoEnd"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts), 
    )

PreSelTauVetoEnd = cms.PSet(
    name = cms.string("PreSelTauVetoEnd"),
    triggers = triggersJetMet,
    cuts = 
    cutsMET + 
    cutsJets + 
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto, 
      cutElecLooseIDVeto,
      cutTauLooseHadronicVeto, 
      ), 
    )  

PreSelElecVetoEndInv = cms.PSet(
    name = cms.string("PreSelElecVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelElecVetoEnd.cuts), 
    )
for cut in PreSelElecVetoEndInv.cuts:
    if cut.cutString == cutElecLooseIDVeto.cutString:
        cut.cutString = cutElecLooseIDVetoInv.cutString
                

PreSelMuonVetoEndInv = cms.PSet(
    name = cms.string("PreSelMuonVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelInvMuonVeto.cuts),  
    )

PreSelTauVetoEndInv = cms.PSet(
    name = cms.string("PreSelTauVetoEndInv"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelTauVetoEnd.cuts),  
    )
for cut in PreSelTauVetoEndInv.cuts:
    if cut.cutString == cutTauLooseHadronicVeto.cutString:
        cut.cutString = cutTauLooseHadronicVetoInv.cutString  


ZMCPart = cms.PSet(
    # Use this to check the Pt of the MC Z particle.
    name = cms.string("ZMCPart"),
    cuts = cms.VPSet (
      cutMCPartPdgZ,
      cutMCPartStatus3, 
      ),
    )

WMCPart = cms.PSet(
    # Use this to check the Pt of the MC W particle.
    name = cms.string("WMCPart"),
    cuts = cms.VPSet (
      cutMCPartPdgW,
      cutMCPartStatus3, 
      ),
    )

WMCPtPostTrig = cms.PSet(
    # Use this to check the Pt of the MC W particle.
    name = cms.string("WMCPtPostTrig"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
      cutMET,
      cutMCPartPdgW,
      cutMCPartStatus3, 
      ),
    )




ZtoMuTrkMuIdNoTrigMet = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdNoTrigMet"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
#        cutMET,
#        cutMETNoMu,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso, 
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        cutTrkPt,
        cutTrkEta,
#       cutTrkEtaBarrel,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )



ZtoMuTrkMetTrig = cms.PSet(
    name = cms.string("ZtoMuTrk"),
    triggers = triggersJetMet,
    cuts =
    cutsTagMuon +
    cms.VPSet (cutMuonPlusMet220) +
    cutsJets + 
    cutsTrkPresel + 
    cms.VPSet (
      cutMuTrkDeltaR,
      cutMuTrkInvMass,
      )
    )

ZtoMuTrkNoVetoNoCalo = cms.PSet(
    name = cms.string("ZtoMuTrkNoVetoNoCalo"),
     triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )

ZtoMuTrkNoVeto = cms.PSet(
    name = cms.string("ZtoMuTrkNoVeto"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      cutMaxCalo10,
      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )

ZtoMuTrkNoVetoPreSel = cms.PSet(
    name = cms.string("ZtoMuTrkNoVetoPreSel"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )




ZtoETrkEIdNoVetoPresel = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoPresel"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto,
#      cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )

NoCrackVetoPreselLoosePt = cms.PSet(
    name = cms.string("NoCrackVetoPreselLoosePt"),
    triggers = triggersSingleElec,
#    cuts = copy.deepcopy(ZtoETrkEIdNoVetoPresel.cuts),
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVetoOrVetoRegion +
    cms.VPSet (
    cutTauLooseHadronicVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    #      cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )

NoCrackVetoElecVeto = cms.PSet(
    name = cms.string("NoCrackVetoElecVeto"),
    triggers = triggersSingleElec,
    #    cuts = copy.deepcopy(ZtoETrkEIdNoVetoPresel.cuts),
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVetoOrVetoRegion +
    cms.VPSet (
    cutTauLooseHadronicVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
    cutElecLooseIDVeto,
    cutTrkDeadEcalVeto,
    #      cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )


ZtoETrkEIdNoVetoPreselLoosePt = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoPreselLoosePt"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdNoVetoPresel.cuts), 
    )
for i in xrange(len(ZtoETrkEIdNoVetoPreselLoosePt.cuts) - 1, -1, -1):
    if ZtoETrkEIdNoVetoPreselLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdNoVetoPreselLoosePt.cuts[i].cutString = cutTrkPt20.cutString

ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdNoVetoPreselLoosePt.cuts), 
    )
for i in xrange(len(ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal.cuts) - 1, -1, -1):
    if ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal.cuts[i].cutString == cutTrkDeadEcalVeto.cutString: 
        del ZtoETrkEIdNoVetoPreselLoosePtNoDeadEcal.cuts[i]


ZtoETrkEIdNoVeto = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVeto"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
    cutTauLooseHadronicVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
#    cutTrkNHits7,
#    cutMaxCalo10,
    cutTrkHitMissOut,

    ) +
    cutsElecTrkZPeak
    )


ZtoMuTauHadNoVeto = cms.PSet(
    name = cms.string("ZtoMuTauHadNoVeto"),
    triggers = triggersSingleMu,
    cuts =
    cutsMuTauHad +
    cms.VPSet (
    cutMuTrkDeltaR,
    cutTrkPt30,
    cutTrkEta2p3,
    ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
#    cutsTrkIso +
    
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutElecLooseIDVeto,
    cutMuonLooseIDVeto,
    cutSecMuonLooseIDVeto,
#    cutTrkHitMissOut,
    ) +
    cutsMuTrkHadZPeak
    )

## ZtoMuTauHadNoTau = cms.PSet(
##     name = cms.string("ZtoMuTauHadNoTau"),
##     triggers = triggersSingleMu,
##     cuts =
##     cutsMuTrk +
##     cms.VPSet (
##     cutMuTrkDeltaR,
##     cutTrkPt30,
##     cutTrkEta2p3,
##     ) +
##     cutsTrkVetoRegions +
##     cutsTrkQuality +
##     #    cutsTrkIso +
    
##     cms.VPSet (
##     cutTrkRelIsoRp3,
##     cutElecLooseIDVeto,
##     cutMuonLooseIDVeto,
##     cutSecMuonLooseIDVeto,
##     #    cutTrkHitMissOut,
##     ) +
##     cutsMuTrkHadZPeak
##     )

ZtoMuTauHad = cms.PSet(
    name = cms.string("ZtoMuTauHad"),
    triggers = triggersSingleMu,
    cuts = cutsMuTrk +
    copy.deepcopy(cutsTrkPresel)+
    cutsMuTrkHadZPeak
    )
for i in xrange(len(ZtoMuTauHad.cuts) - 1, -1, -1):
    if ZtoMuTauHad.cuts[i].cutString == cutTrkPt.cutString:
                ZtoMuTauHad.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTauHadWithEcalo = cms.PSet(
    name = cms.string("ZtoMuTauHadEcalo"),
    triggers = triggersSingleMu,
    cuts = cutsMuTrk +
    copy.deepcopy(cutsTrkPreselSigReg)+
    cutsMuTrkHadZPeak
    )
for i in xrange(len(ZtoMuTauHadWithEcalo.cuts) - 1, -1, -1):
    if ZtoMuTauHadWithEcalo.cuts[i].cutString == cutTrkPt.cutString:
        ZtoMuTauHadWithEcalo.cuts[i].cutString = cutTrkPt30.cutString
    if ZtoMuTauHadWithEcalo.cuts[i].cutString == cutTrkHitMissOut.cutString:
        del ZtoMuTauHadWithEcalo.cuts[i]
    if ZtoMuTauHadWithEcalo.cuts[i].cutString == cutTrkJetDeltaR.cutString:
        del ZtoMuTauHadWithEcalo.cuts[i]


ZtoMuTauHadNoTauVetoWithEcalo = cms.PSet(
    name = cms.string("ZtoMuTauHadNoTauVetoEcalo"),
    triggers = triggersSingleMu,
    cuts = cutsMuTrk +
    copy.deepcopy(cutsTrkPreselSigReg)+
    cutsMuTrkHadZPeak
    )
for i in xrange(len(ZtoMuTauHadNoTauVetoWithEcalo.cuts) - 1, -1, -1):
    if ZtoMuTauHadNoTauVetoWithEcalo.cuts[i].cutString == cutTrkPt.cutString:
        ZtoMuTauHadNoTauVetoWithEcalo.cuts[i].cutString = cutTrkPt30.cutString
    if ZtoMuTauHadNoTauVetoWithEcalo.cuts[i].cutString == cutTrkHitMissOut.cutString:
        del ZtoMuTauHadNoTauVetoWithEcalo.cuts[i]
    if ZtoMuTauHadNoTauVetoWithEcalo.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        del ZtoMuTauHadNoTauVetoWithEcalo.cuts[i]
    if ZtoMuTauHadNoTauVetoWithEcalo.cuts[i].cutString == cutTrkJetDeltaR.cutString:
                del ZtoMuTauHadNoTauVetoWithEcalo.cuts[i]
            
            
ZtoMuTauHadNoTrkJetDeltaR = cms.PSet(
    name = cms.string("ZtoMuTauHadNoTrkJetDeltaR"),
    triggers = triggersSingleMu,
    cuts = cutsMuTrk +
    copy.deepcopy(cutsTrkPresel)+
    cutsMuTrkHadZPeak
    )
for i in xrange(len(ZtoMuTauHadNoTrkJetDeltaR.cuts) - 1, -1, -1):
    if ZtoMuTauHadNoTrkJetDeltaR.cuts[i].cutString == cutTrkPt.cutString:
        ZtoMuTauHadNoTrkJetDeltaR.cuts[i].cutString = cutTrkPt30.cutString
    if ZtoMuTauHadNoTrkJetDeltaR.cuts[i].cutString == cutTrkJetDeltaR.cutString:
       del ZtoMuTauHadNoTrkJetDeltaR.cuts[i]

ZtoMuTauHadNoTau = cms.PSet(
    name = cms.string("ZtoMuTauHadNoTau"),
    triggers = triggersSingleMu,
    cuts = copy.deepcopy(ZtoMuTauHad.cuts)
    )
for i in xrange(len(ZtoMuTauHadNoTau.cuts) - 1, -1, -1):
    if ZtoMuTauHadNoTau.cuts[i].cutString == cutTrkPt.cutString:
        ZtoMuTauHadNoTau.cuts[i].cutString = cutTrkPt30.cutString
    if ZtoMuTauHadNoTau.cuts[i].cutString == cutTrkJetDeltaR.cutString \
    or ZtoMuTauHadNoTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        del ZtoMuTauHadNoTau.cuts[i]
            
MuTauHadCtrl = cms.PSet(
    name = cms.string("MuTauHadCtrl"),
    triggers = triggersSingleMu,
    cuts =
    cutsMuTrk +
    cms.VPSet (
    #cutMuTrkDeltaR,
    cutTrkPt30,
    cutTrkEta2p3,
    ) +
    cutsTrkVetoRegions +
    cutsTrkQuality +
    #    cutsTrkIso +
    
    cms.VPSet (
    cutTrkRelIsoRp3,
    cutElecLooseIDVeto,
    #   cutMuonLooseIDVeto,
    #   cutSecMuonLooseIDVeto,
    #    cutTrkHitMissOut,
    ) 
    #cutsMuTrkHadZPeak
    )



## ZtoMuTauHad = cms.PSet(
##     name = cms.string("ZtoMuTauHad"),
##     triggers = triggersSingleMu,
##     cuts =
##     cutsMuTrk +
##     cms.VPSet (
##     cutTrkPt30,
##     cutTrkEta2p3,
##     ) +
##     cutsTrkVetoRegions +
##     cutsTrkQuality +
##     cutsTrkIso +
##     cutsTrkLeptonVetoNoMu  +
##     cutsMuTrkHadZPeak
##     )



ZtoETrkEIdNoVetoNoMissOut = cms.PSet(
    name = cms.string("ZtoETrkEIdNoVetoNoMissOut"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutMuonLooseIDVeto,
      cutSecMuonLooseIDVeto,
    ) +
    cutsElecTrkZPeak
    )


ZtoMuTrk = cms.PSet(
    name = cms.string("ZtoMuTrk"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPresel +
    cms.VPSet (
      cutMaxCalo10,
      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )

ZtoMuTrkPreSel = cms.PSet(
    name = cms.string("ZtoMuTrkPreSel"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPresel +
    cutsMuTrkZPeak
    )

ZtoETrkEId = cms.PSet(
    name = cms.string("ZtoETrkEId"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPreselNoLepVeto +
    cms.VPSet (
#      cutMaxCalo10,
      cutTrkHitMissOut6,
    ) +
    cutsElecTrkZPeak
    )

ZtoETrkEIdPresel = cms.PSet(
    name = cms.string("ZtoETrkEIdPresel"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPresel +
    cms.VPSet (
#    cutMaxCalo10,
#    cutTrkHitMissOut,
    ) +
    cutsElecTrkZPeak
    )

ZtoETrkEIdPresel7Hits = cms.PSet(
    name = cms.string("ZtoETrkEIdPresel7Hits"),
    triggers = triggersSingleElec,
    cuts =
    cutsTagElec +
    cutsTrkPresel +
    cms.VPSet(
    cutTrkNHits
    ) + 
    cutsElecTrkZPeak
    )


ZtoETrkEIdPreselMaxCalo = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselMaxCalo"),
    triggers = triggersSingleElec,
    cuts =
      cutsTagElec +
      cutsTrkPresel +
      cms.VPSet (
      cutMaxCalo10,
      ) +
    cutsElecTrkZPeak
    )

            
                        
ZtoETrkEIdPreselLoosePt7Hits = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselLoosePt7Hits"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdPresel7Hits.cuts),
    )
for i in xrange(len(ZtoETrkEIdPreselLoosePt7Hits.cuts) - 1, -1, -1):
    if ZtoETrkEIdPreselLoosePt7Hits.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdPreselLoosePt7Hits.cuts[i].cutString = cutTrkPt20.cutString

ZtoETrkEIdPreselLoosePtMaxCalo = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselLoosePtMaxCalo"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdPreselMaxCalo.cuts),
    )
for i in xrange(len(ZtoETrkEIdPreselLoosePtMaxCalo.cuts) - 1, -1, -1):
    if ZtoETrkEIdPreselLoosePtMaxCalo.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdPreselLoosePtMaxCalo.cuts[i].cutString = cutTrkPt20.cutString

ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo"),
    triggers = triggersSingleElec,
    cuts = copy.deepcopy(ZtoETrkEIdPreselMaxCalo.cuts),
    )
for i in xrange(len(ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo.cuts) - 1, -1, -1):
    if ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo.cuts[i].cutString = cutTrkPt20.cutString
    if ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo.cuts[i].cutString == cutTrkDeadEcalVeto.cutString: # replace pt>50 with pt>20 cut
        del ZtoETrkEIdPreselLoosePtNoDeadEcalMaxCalo.cuts[i]


ZtoETrkEIdPreselMaxCaloNMissOut3 = cms.PSet(
    name = cms.string("ZtoETrkEIdPreselMaxCaloNMissOu3"),
    triggers = triggersSingleElec,
    cuts =
      cutsTagElec +
      cutsTrkPresel +
      cms.VPSet (
      cutTrkNHits,
      cutMaxCalo10,
      cutTrkHitMissOut, 
      ) +
      cutsElecTrkZPeak
    )


ZtoMuTrkPreSelLoosePt = copy.deepcopy(ZtoMuTrkPreSel)
ZtoMuTrkPreSelLoosePt.name = "ZtoMuTrkPreSelLoosePt"
for i in xrange(len(ZtoMuTrkPreSelLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkPreSelLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>30 cut
        ZtoMuTrkPreSelLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkPreSelLoosePtNoFiducial = copy.deepcopy(ZtoMuTrkPreSelLoosePt)
ZtoMuTrkPreSelLoosePtNoFiducial.name = "ZtoMuTrkPreSelLoosePtNoFiducial"
for i in xrange(len(ZtoMuTrkPreSelLoosePtNoFiducial.cuts) - 1, -1, -1):
    if ZtoMuTrkPreSelLoosePtNoFiducial.cuts[i].cutString == cutTrkWheel0GapVeto.cutString or \
       ZtoMuTrkPreSelLoosePtNoFiducial.cuts[i].cutString == cutTrkEtaMuonPk.cutString or \
       ZtoMuTrkPreSelLoosePtNoFiducial.cuts[i].cutString == cutTrkCrackVeto.cutString or \
       ZtoMuTrkPreSelLoosePtNoFiducial.cuts[i].cutString == cutTrkDeadEcalVeto.cutString or \
       ZtoMuTrkPreSelLoosePtNoFiducial.cuts[i].cutString == cutTrkBadCSCVeto.cutString: 
        del ZtoMuTrkPreSelLoosePtNoFiducial.cuts[i]  

ZtoMuTrkNoVetoPreSelLoosePt = copy.deepcopy(ZtoMuTrkNoVetoPreSel)
ZtoMuTrkNoVetoPreSelLoosePt.name = "ZtoMuTrkNoVetoPreSelLoosePt"
for i in xrange(len(ZtoMuTrkNoVetoPreSelLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoVetoPreSelLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkNoVetoPreSelLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkLoosePt = copy.deepcopy(ZtoMuTrk)
ZtoMuTrkLoosePt.name = "ZtoMuTrkLoosePt"
for i in xrange(len(ZtoMuTrkLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkNoVetoLoosePt = copy.deepcopy(ZtoMuTrkNoVeto)
ZtoMuTrkNoVetoLoosePt.name = "ZtoMuTrkNoVetoLoosePt"
for i in xrange(len(ZtoMuTrkNoVetoLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoVetoLoosePt.cuts[i].cutString == cutTrkPt.cutString: # replace pt>50 with pt>20 cut
        ZtoMuTrkNoVetoLoosePt.cuts[i].cutString = cutTrkPt30.cutString

ZtoMuTrkNoMissOutLoosePt = copy.deepcopy(ZtoMuTrkLoosePt)
ZtoMuTrkNoMissOutLoosePt.name = "ZtoMuTrkNoMissOutLoosePt"
for i in xrange(len(ZtoMuTrkNoMissOutLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoMissOutLoosePt.cuts[i].cutString == cutTrkHitMissOut.cutString: 
        del ZtoMuTrkNoMissOutLoosePt.cuts[i] 

ZtoMuTrkNoMissOutNoVetoLoosePt = copy.deepcopy(ZtoMuTrkNoVetoLoosePt)
ZtoMuTrkNoMissOutNoVetoLoosePt.name = "ZtoMuTrkNoMissOutNoVetoLoosePt"
for i in xrange(len(ZtoMuTrkNoMissOutNoVetoLoosePt.cuts) - 1, -1, -1):
    if ZtoMuTrkNoMissOutNoVetoLoosePt.cuts[i].cutString == cutTrkHitMissOut.cutString: 
        del ZtoMuTrkNoMissOutNoVetoLoosePt.cuts[i] 

                



ZtoMuTrkNoMuCutsNoVeto = cms.PSet(
    name = cms.string("ZtoMuTrkNoMuCutsNoVeto"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon + 
    cutsTrkPreselNoMuCutsNoLepVeto + 
    cms.VPSet (
      cutTauLooseHadronicVeto,
      cutElecLooseIDVeto,
      cutMaxCalo10,
      #      cutTrkHitMissOut,
      ) + 
    cutsMuTrkZPeak
    )


ZtoMuTrkNoMuCuts = cms.PSet(
    name = cms.string("ZtoMuTrkNoMuCuts"),
    triggers = triggersSingleMu, 
    cuts = 
    cutsTagMuon +
    cutsTrkPreselNoMuCuts +
    cms.VPSet (
      cutMaxCalo10,
      #      cutTrkHitMissOut,
##       cutMuonLooseIDVeto,
##       cutSecMuonLooseIDVeto,
      ) + 
    cutsMuTrkZPeak
    )



ZtoMuTrkMuIdHiStats = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdHiStats"),
#    triggers = triggersJetMetOrSingleMu, 
     triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
#       cutMETNoMu,
       cutMET,
#       cutMuonChgNeg,
#       cutMuonChgPos,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
#       cutTrkMuonId, 
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
#        cutMuTrkInvMass,
        cutMuTrkInvMass80To100, 
        cutMuTrkChgOpp, 
        cutMuTrkDeltaR,
        cutTrkHitMissOut,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        ),
    )

ZtoMuTrkMuIdInvHits = cms.PSet(
    name = cms.string("ZtoMuTrkMuIdInvHits"),
#    triggers = triggersJetMetOrSingleMu, 
     triggers = triggersJetMet,
#    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMET,
#       cutMETNoMu,
#       cutMuonChgNeg,
#       cutMuonChgPos,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        cutMuTrkChgOpp, 
        cutTrkPt50,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        cutTrkWheel0GapVeto,
        cutTrkEtaMuonPk,
        cutMaxCalo10, 
        cutTrkHitMissOutInv,
        ),
    )

## ZtoMuTrkMuId = copy.deepcopy(ZtoMuTrkMuIdNoVeto)  
## ZtoMuTrkMuId.name = "ZtoMuTrkMuId"  
## ZtoMuTrkMuId.cuts.append(cutMuonLooseIDVeto)
## ZtoMuTrkMuId.cuts.append(cutSecMuonLooseIDVeto)


## Ctrl sample for muons ##
ZtoMuTrkInvMuonVeto = cms.PSet(
    name = cms.string("ZtoMuTrkInvMuonVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        # See SMP-12-023 for example of W->mu nu selection  
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonPFIso,
        cutMuonPlusMet220, 
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
#       cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutMuonLooseIDVetoInv,
        cutMuTrkDeltaR,
        cutMuTrkInvMass,
        ),
    )

BadCSCVetoRegions = cms.PSet(
    name = cms.string("BadCSCVetoRegions"),
    cuts = cms.VPSet (
      cutTrkBadCSCVetoInv, 
      ) 
    )  


FakeTrackSel = cms.PSet(
    name = cms.string("FakeTrackSel"),
    cuts = cms.VPSet (
      cutTrkNotGenMatched,
      ) +
      cutsTrkPtEta + 
      cutsTrkVetoRegions + 
      cms.VPSet (
      cutTrkDZ,
      cutTrkHitMissIn, 
      ) + 
      cutsTrkIso + 
      cutsTrkLeptonVeto
    )  



FullSelectionInvD0 = cms.PSet(
    name = cms.string("FullSelectionInvD0"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0Loose = cms.PSet(
    name = cms.string("FullSelectionInvD0Loose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZ = cms.PSet(
    name = cms.string("FullSelectionInvDZ"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZLoose = cms.PSet(
    name = cms.string("FullSelectionInvDZLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHitsIs4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNHitsLoose = cms.PSet(
    name = cms.string("FullSelectionInvNHitsLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHitsIs4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNMissMidLoose = cms.PSet(
    name = cms.string("FullSelectionInvNMissMidLoose"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET100,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvNoneLoose = cms.PSet(
    name = cms.string("FullSelectionInvNoneLoose"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET100,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvDZ = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZ"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNHits = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHitsIs4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHitsIs4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvDZInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHitsIs4,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)

FullSelectionInvD0InvDZInvNHits = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHitsIs4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvD0InvDZInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHits,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZ,
        cutTrkNHitsIs4,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



FullSelectionInvDZInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvDZInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZInv,
        cutTrkNHitsIs4,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionInvD0InvDZInvNHitsInvNMissMid = cms.PSet(
    name = cms.string("FullSelectionInvD0InvDZInvNHitsInvNMissMid"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0Inv,
        cutTrkDZInv,
        cutTrkNHitsIs4,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)



MuTrigNoCuts = cms.PSet(
    name = cms.string("MuTrigNoCuts"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
       cutNoCuts,
       )
    )

FakeTrkMuTrig = cms.PSet(
    name = cms.string("FakeTrkMuTrig"),
    triggers = triggersSingleMu,
    cuts = cms.VPSet (
#        cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
        cutTrkNotGenMatched,  
    )
)



FakeTrkTestCorr = cms.PSet(
    name = cms.string("FakeTrkTestCorr"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
#        cutTrkD0,
#        cutTrkDZ,
#        cutTrkNHits,
#        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FakeTrkTestCorrLoose = cms.PSet(
    name = cms.string("FakeTrkTestCorrLoose"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
#        cutTrkD0,
#        cutTrkDZ,
#        cutTrkNHits,
#        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionFakeTrkCtrlInv = cms.PSet(
    name = cms.string("FullSelectionFakeTrkCtrlInv"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
#       cutTrkD0Inv,
        cutTrkDZ,
#       cutTrkDZInv,
#       cutTrkNHits,
        cutTrkNHitsIs4,
#        cutTrkHitMissMid,
        cutTrkHitMissMidInv,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)


FullSelectionFakeTrkCtrlNom = cms.PSet(
    name = cms.string("FullSelectionFakeTrkCtrlNom"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
#       cutTrkD0Inv,
        cutTrkDZ,
#       cutTrkDZInv,
#       cutTrkNHits,
        cutTrkNHitsIs4,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutMaxCalo10, 
        cutTrkHitMissOut,
    )
)





PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutElecLooseIDVeto,
       cutMuonLooseIDVeto,
       ),
    )



PreSelectionMuonLooseID = cms.PSet(
    name = cms.string("PreSelectionMuonLooseID"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
       cutMET,
       cutSecJetPt,
       cutSecJetEta2p4,
       cutSecJetNoiseChgHad,
       cutSecJetNoiseChgEM,
       cutSecJetNoiseNeuHad,
       cutSecJetNoiseNeuEM,
       cutSubLeadingJetID,
       cutElecLooseIDVeto,
       cutMuonLooseID,
       cutTauLooseHadronicVeto,
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkDeadEcalVeto,
       cutTrkCrackVeto,
       cutTrkRelIsoRp3,
       cutTrkJetDeltaR,
       cutJetJetDPhi,
       ),
    )




## Ctrl sample for electrons ##
PreSelectionPt30NoLepVeto = cms.PSet(
    name = cms.string("PreSelectionPt30NoLepVeto"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionPt30NoLepVeto.cuts) - 1, -1, -1):
    if PreSelectionPt30NoLepVeto.cuts[i].cutString == cutTrkPt.cutString:
        PreSelectionPt30NoLepVeto.cuts[i].cutString = cutTrkPt30.cutString
    if PreSelectionPt30NoLepVeto.cuts[i].cutString == cutElecLooseIDVeto.cutString \
    or PreSelectionPt30NoLepVeto.cuts[i].cutString == cutTauLooseHadronicVeto.cutString \
    or PreSelectionPt30NoLepVeto.cuts[i].cutString == cutMuonLooseIDVeto.cutString \
    or PreSelectionPt30NoLepVeto.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString:  
        del PreSelectionPt30NoLepVeto.cuts[i] 


## Ctrl sample for electrons ##
PreSelectionElec = cms.PSet(
    name = cms.string("PreSelectionElec"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionElec.cuts) - 1, -1, -1):
    if PreSelectionElec.cuts[i].cutString == cutElecLooseIDVeto.cutString: 
        del PreSelectionElec.cuts[i] 

PreSelectionElecPt30 = copy.deepcopy(PreSelectionElec)
PreSelectionElecPt30.name = cms.string("PreSelectionElecPt30")
for i in xrange(len(PreSelectionElecPt30.cuts) - 1, -1, -1):
    if PreSelectionElecPt30.cuts[i].cutString == cutTrkPt.cutString: 
        PreSelectionElecPt30.cuts[i].cutString = cutTrkPt30.cutString  

PreSelectionElecNoTrig = cms.PSet(
    name = cms.string("PreSelectionElecNoTrig"),
    cuts = copy.deepcopy(PreSelectionElec.cuts), 
    )

## Ctrl sample for muons ##
PreSelectionMuon = cms.PSet(
    name = cms.string("PreSelectionMuon"),  
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionMuon.cuts) - 1, -1, -1):
    if PreSelectionMuon.cuts[i].cutString == cutMuonLooseIDVeto.cutString or PreSelectionMuon.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString: 
        del PreSelectionMuon.cuts[i] 

## Use MetNoMu instead of Met cut ## 
PreSelectionMuonMetNoMu = cms.PSet(
    name = cms.string("PreSelectionMuonMetNoMu"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuon.cuts), 
    )
for i in xrange(len(PreSelectionMuonMetNoMu.cuts) - 1, -1, -1):
    if PreSelectionMuonMetNoMu.cuts[i].cutString == cutMET.cutString:
        PreSelectionMuonMetNoMu.cuts[i].cutString = cutMETNoMu.cutString    

PreSelectionMuonNoTrig = cms.PSet(
    name = cms.string("PreSelectionMuonNoTrig"),
    cuts = copy.deepcopy(PreSelectionMuon.cuts), 
    )

PreSelectionMuonNoMissInMid = copy.deepcopy(PreSelectionMuon)
PreSelectionMuonNoMissInMid.name = cms.string("PreSelectionMuonNoMissInMid")
for i in xrange(len(PreSelectionMuonNoMissInMid.cuts) - 1, -1, -1):
    if PreSelectionMuonNoMissInMid.cuts[i].cutString == cutTrkHitMissIn.cutString or PreSelectionMuonNoMissInMid.cuts[i].cutString == cutTrkHitMissMid.cutString:
        del PreSelectionMuonNoMissInMid.cuts[i]



## Ctrl sample for taus ##
PreSelectionTau = cms.PSet(
    name = cms.string("PreSelectionTau"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(cutsPresel), 
    )
for i in xrange(len(PreSelectionTau.cuts) - 1, -1, -1):
    if PreSelectionTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:  
        del PreSelectionTau.cuts[i]



PreSelectionPTrkJetDeltaR = cms.PSet(
    name = cms.string("PreSelectionPTrkJetDeltaR"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutMET,
         cutSecJetPt,
         cutSecJetEta2p4,
         cutSecJetNoiseChgHad,
         cutSecJetNoiseChgEM,
         cutSecJetNoiseNeuHad,
         cutSecJetNoiseNeuEM,
         cutSubLeadingJetID,
         cutElecLooseIDVeto,
         cutMuonLooseIDVeto,
         cutTauLooseHadronicVeto,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         cutTrkJetDeltaR
         ),
    )


PreSelectionWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
## PreSelectionWithTrigJetMet.cuts.insert(0,cutJetPt)
## PreSelectionWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionDeadEcalMatch = cms.PSet(
        name = cms.string("PreSelectionDeadEcalMatch"),
        cuts = cms.VPSet (
           cutTrkPt,
           cutTrkEta,
           cutTrkD0,
           cutTrkDZ,
           cutTrkNHits,
           cutTrkHitMissMid,
           cutTrkHitMissIn,
           cutTrkIso,
           cutMuonVeto,
           cutElecVeto,
           cutTrkDeadEcalMatch,
           cutTrkCrackVeto,
           ),
        )

PreSelectionDeadEcalMatchWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionDeadEcalMatchWithTrigJetMet"),
        triggers = triggersJetMet,
        cuts = copy.deepcopy(PreSelectionDeadEcalMatch.cuts),
        )
PreSelectionDeadEcalMatchWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalMatchWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnly = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnly"),
    cuts = cms.VPSet (
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         ),
    )

PreSelectionIsoTrkOnlyWithNoiseClean = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithNoiseClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutEvtFilterScraping,
         cutVtxGood,
         cutMET,
         cutJetPt,
         cutJetEta,
         cutJetNoiseChgHad,
         cutJetNoiseNeuEM,
         cutJetNoiseNeuHad,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         cutTrkSumPtLT,
         ),
    )

PreSelectionWithNoiseClean = cms.PSet(
    name = cms.string("PreSelectionWithNoiseClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
         cutEvtFilterScraping,
         cutVtxGood,
         cutMET,
         cutJetPt,
         cutJetEta,
         cutJetNoiseChgHad,
         cutJetNoiseNeuEM,
         cutJetNoiseNeuHad,
         cutTrkPt,
         cutTrkEta,
         cutTrkD0,
         cutTrkDZ,
         cutTrkNHits,
         cutTrkHitMissMid,
         cutTrkHitMissIn,
         cutTrkIso,
         cutTrkSumPtLT,
         cutMuonVeto,
         cutElecVeto,
         cutTrkDeadEcalVeto,
         cutTrkCrackVeto,
         ),
    )

PreSelectionIsoTrkOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnly.cuts),
    )
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyElecMatch = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyElecMatch"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutElecPt20,     
        cutElecEta,    
        cutElecD0,     
        cutElecMva, 
        #        cutElecTightID,  
        cutElecPFIso,  
        cutElecNHits,  
        cutElecVetoOneMax, 
        cutMuonVetoPt10,   
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        #        cutTrkDZ,
        cutTrkNHits,
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn,
        ## cutTrkIso,
        ## cutTrkSumPtLT,
        cutElecTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyMuonMatch = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyMuonMatch"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutEvtFilterScraping,
        cutVtxGood, 
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
        cutNJets,
        cutMuonPt20,
        cutMuonEta,
        cutMuonTightID,
        cutMuonDetIso,
        cutMuonOneOnly,
        cutElecVetoPt10,   
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        #        cutTrkDZ,
        cutTrkNHits,
        ## cutTrkHitMissMid,
        ## cutTrkHitMissIn,
        #        cutTrkIso,
        #        cutTrkSumPtLT,
        cutMuonTrkDRSame,
    )
)


PreSelectionIsoTrkOnlyNoMuonMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoMuonMatch.name = "PreSelectionIsoTrkOnlyNoMuonMatch"
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonTrkDRSameNone)
PreSelectionIsoTrkOnlyNoMuonMatch.cuts.append(cutMuonVeto)

PreSelectionIsoTrkOnlyNoElecMatch = copy.deepcopy(PreSelectionIsoTrkOnlyWithTrigJetMet)
PreSelectionIsoTrkOnlyNoElecMatch.name = "PreSelectionIsoTrkOnlyNoElecMatch"
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutTrkDeadEcalVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutTrkCrackVeto)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecTrkDRSameNone)
PreSelectionIsoTrkOnlyNoElecMatch.cuts.append(cutElecVeto)




PreSelectionIsoTrkOnlyNoDz = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoDzWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDzWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoDz.cuts),
    )
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoDzWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoD0 = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoDz"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoD0WithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoD0WithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoD0.cuts),
    )
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoD0WithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnly = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnly"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       cutMuonVeto,
       ),
    )

PreSelectionMuonVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnly.cuts),
    )
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionElectronVetoOnly = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnly"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       ),
    )

PreSelectionElectronVetoOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionElectronVetoOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionElectronVetoOnly.cuts),
    )
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionElectronVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionDeadEcalVetoOnly = cms.PSet(
        name = cms.string("PreSelectionDeadEcalVetoOnly"),
        cuts = cms.VPSet (
           cutTrkPt,
           cutTrkEta,
           cutTrkD0,
           cutTrkDZ,
           cutTrkNHits,
           cutTrkHitMissMid,
           cutTrkHitMissIn,
           cutTrkIso,
           cutMuonVeto,
           cutElecVeto,
           cutTrkDeadEcalVeto,
           ),
        )

PreSelectionDeadEcalVetoOnlyWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionDeadEcalVetoOnlyWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionDeadEcalVetoOnly.cuts),
            )
PreSelectionDeadEcalVetoOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalVetoOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionDeadEcalMatchOnly = cms.PSet(
            name = cms.string("PreSelectionDeadEcalMatchOnly"),
            cuts = cms.VPSet (
               cutTrkPt,
               cutTrkEta,
               cutTrkD0,
               cutTrkDZ,
               cutTrkNHits,
               cutTrkHitMissMid,
               cutTrkHitMissIn,
               cutTrkIso,
               cutMuonVeto,
               cutElecVeto,
               cutTrkDeadEcalMatch,
               ),
            )

PreSelectionDeadEcalMatchOnlyWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionDeadEcalMatchOnlyWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionDeadEcalMatchOnly.cuts),
    )
PreSelectionDeadEcalMatchOnlyWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionDeadEcalMatchOnlyWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionIsoTrkOnlyDzSide = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSide"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZSide,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyDzSideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyDzSideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyD0Side = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0Side"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0Side,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkHitMissMid,
       cutTrkHitMissIn,
       cutTrkIso,
       ),
    )
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyD0SideWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),
    )
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyD0SideWithTrigJetMet.cuts.insert(0,cutMET)


PreSelIdMuonNoVeto = cms.PSet(
    name = cms.string("PreSelIdMuonNoVeto"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
##         cutMET,
##         cutMETNoMu,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
##         cutSubLeadingJetID,
##         cutJetJetDPhi,
        cutTrkMuonId, 
#       cutMET,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMaxCalo10, 
##         cutTrkHitMissOut,
    )
)


PreSelCtrlNMiss = copy.deepcopy(PreSelection)
PreSelCtrlNMiss.name = "PreSelCtrlNMiss"
PreSelCtrlNMiss.cuts = cutsPreselCtrlNMiss 

PreSelCtrlNMissIdElec = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdElec.name = "PreSelCtrlNMissIdElec"
PreSelCtrlNMissIdElec.cuts.append(cutTrkElectronId) 

PreSelCtrlNMissIdMuon = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdMuon.name = "PreSelCtrlNMissIdMuon"
PreSelCtrlNMissIdMuon.cuts.append(cutTrkMuonId) 

PreSelCtrlNMissIdTau = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdTau.name = "PreSelCtrlNMissIdTau"
PreSelCtrlNMissIdTau.cuts.append(cutTrkTauId) 

PreSelCtrlNMissIdFake = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdFake.name = "PreSelCtrlNMissIdFake"
PreSelCtrlNMissIdFake.cuts.append(cutTrkNotGenMatched)  

PreSelCtrlNMissIdOther = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissIdOther.name = "PreSelCtrlNMissIdOther"
PreSelCtrlNMissIdOther.cuts = PreSelCtrlNMissIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet

PreSelCtrlNMissElec = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissElec.name = "PreSelCtrlNMissElec"
for i in xrange(len(PreSelCtrlNMissElec.cuts) - 1, -1, -1):
    if PreSelCtrlNMissElec.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del PreSelCtrlNMissElec.cuts[i]

PreSelCtrlNMissMuon = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissMuon.name = "PreSelCtrlNMissMuon"
for i in xrange(len(PreSelCtrlNMissMuon.cuts) - 1, -1, -1):
    if PreSelCtrlNMissMuon.cuts[i].cutString == cutMuonLooseIDVeto.cutString or PreSelCtrlNMissMuon.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString: 
        del PreSelCtrlNMissMuon.cuts[i]

PreSelCtrlNMissTau = copy.deepcopy(PreSelCtrlNMiss)
PreSelCtrlNMissTau.name = "PreSelCtrlNMissTau"
for i in xrange(len(PreSelCtrlNMissTau.cuts) - 1, -1, -1):
    if PreSelCtrlNMissTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        del PreSelCtrlNMissTau.cuts[i]


PreSelCtrlEcalo = copy.deepcopy(PreSelection)
PreSelCtrlEcalo.name = "PreSelCtrlEcalo"
PreSelCtrlEcalo.cuts = cutsPreselCtrlEcalo 

PreSelCtrlEcaloIdElec = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdElec.name = "PreSelCtrlEcaloIdElec"
PreSelCtrlEcaloIdElec.cuts.append(cutTrkElectronId) 

PreSelCtrlEcaloIdMuon = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdMuon.name = "PreSelCtrlEcaloIdMuon"
PreSelCtrlEcaloIdMuon.cuts.append(cutTrkMuonId) 

PreSelCtrlEcaloIdTau = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdTau.name = "PreSelCtrlEcaloIdTau"
PreSelCtrlEcaloIdTau.cuts.append(cutTrkTauId) 

PreSelCtrlEcaloIdFake = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdFake.name = "PreSelCtrlEcaloIdFake"
PreSelCtrlEcaloIdFake.cuts.append(cutTrkNotGenMatched)  

PreSelCtrlEcaloIdOther = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloIdOther.name = "PreSelCtrlEcaloIdOther"
PreSelCtrlEcaloIdOther.cuts = PreSelCtrlEcaloIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet

PreSelCtrlEcaloElec = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloElec.name = "PreSelCtrlEcaloElec"
for i in xrange(len(PreSelCtrlEcaloElec.cuts) - 1, -1, -1):
    if PreSelCtrlEcaloElec.cuts[i].cutString == cutElecLooseIDVeto.cutString:
        del PreSelCtrlEcaloElec.cuts[i]

PreSelCtrlEcaloMuon = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloMuon.name = "PreSelCtrlEcaloMuon"
for i in xrange(len(PreSelCtrlEcaloMuon.cuts) - 1, -1, -1):
    if PreSelCtrlEcaloMuon.cuts[i].cutString == cutMuonLooseIDVeto.cutString or PreSelCtrlEcaloMuon.cuts[i].cutString == cutSecMuonLooseIDVeto.cutString: 
        del PreSelCtrlEcaloMuon.cuts[i]

PreSelCtrlEcaloTau = copy.deepcopy(PreSelCtrlEcalo)
PreSelCtrlEcaloTau.name = "PreSelCtrlEcaloTau"
for i in xrange(len(PreSelCtrlEcaloTau.cuts) - 1, -1, -1):
    if PreSelCtrlEcaloTau.cuts[i].cutString == cutTauLooseHadronicVeto.cutString:
        del PreSelCtrlEcaloTau.cuts[i]


PreSelIdElec = copy.deepcopy(PreSelection)
PreSelIdElec.name = "PreSelIdElec"
PreSelIdElec.cuts.append(cutTrkElectronId)

PreSelIdMuon = copy.deepcopy(PreSelection)
PreSelIdMuon.name = "PreSelIdMuon"
PreSelIdMuon.cuts.append(cutTrkMuonId)

PreSelIdTau = copy.deepcopy(PreSelection)
PreSelIdTau.name = "PreSelIdTau"
PreSelIdTau.cuts.append(cutTrkTauId)

PreSelIdFake = copy.deepcopy(PreSelection)
PreSelIdFake.name = "PreSelIdFake"
PreSelIdFake.cuts.append(cutTrkNotGenMatched)

PreSelIdOther = copy.deepcopy(PreSelection)
PreSelIdOther.name = "PreSelIdOther"
PreSelIdOther.cuts = PreSelIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet 



FullSelIdElec = copy.deepcopy(FullSelection)
FullSelIdElec.name = "FullSelIdElec"
for i in range(0, len(FullSelIdElec.cuts)):
    if FullSelIdElec.cuts[i].cutString == cutTrkPt.cutString:
        idx = i
FullSelIdElec.cuts.insert(idx, cutTrkElectronId)

FullSelIdMuon = copy.deepcopy(FullSelection)
FullSelIdMuon.name = "FullSelIdMuon"
FullSelIdMuon.cuts.insert(idx, cutTrkMuonId)

FullSelIdTau = copy.deepcopy(FullSelection)
FullSelIdTau.name = "FullSelIdTau"
FullSelIdTau.cuts.insert(idx, cutTrkTauId)

FullSelIdFake = copy.deepcopy(FullSelection)
FullSelIdFake.name = "FullSelIdFake"
FullSelIdFake.cuts.insert(idx, cutTrkNotGenMatched)

FullSelIdOther = copy.deepcopy(FullSelection)
FullSelIdOther.name = "FullSelIdOther"
FullSelIdOther.cuts = FullSelIdOther.cuts + cutsTrkIdOther # Cannot append a VPSet 



PreSelIdMuonInvHits = cms.PSet(
    name = cms.string("PreSelIdMuonInvHits"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
#        cutMETNoMu,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
#       cutTrkMuonId, 
#       cutTrkPt,
        cutTrkPt50,
        cutTrkEta,
#       cutTrkEtaBarrel,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto, 
        cutTauLooseHadronicVeto,  
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto, 
        cutTrkWheel0GapVeto, 
        cutTrkEtaMuonPk, 
        cutMaxCalo10, 
        cutTrkHitMissOutInv,
    )
)

SimpleIdMuon = cms.PSet(
    name = cms.string("SimpleIdMuon"),
#    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId, 
#        cutTrkPt,
        cutTrkPt50,
#       cutTrkPt75,
        cutTrkEta,
        cutMuonLooseIDVeto,
        cutSecMuonLooseIDVeto,
        )
    )


PreSelIdMuonNoMetJetNoVeto = cms.PSet(
    name = cms.string("PreSelIdMuonNoMetJetNoVeto"),
    triggers = triggersSingleMu, 
    cuts = cms.VPSet (
##         cutMET,
##         cutSecJetPt,
##         cutSecJetEta2p4,            
##         cutSecJetNoiseChgHad,
##         cutSecJetNoiseChgEM,
##         cutSecJetNoiseNeuHad,
##         cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
#       cutTrkEtaBarrel,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,    
    )
)

PreSelIdMuonNoMetJet = copy.deepcopy(PreSelIdMuonNoMetJetNoVeto)  
PreSelIdMuonNoMetJet.name = "PreSelIdMuonNoMetJet"  
PreSelIdMuonNoMetJet.cuts.append(cutMuonLooseIDVeto)  
PreSelIdMuonNoMetJet.cuts.append(cutSecMuonLooseIDVeto)  



SigRegIdMuon = cms.PSet(
    name = cms.string("SigRegIdMuon"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,    
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkHitMissOut,
        cutMaxCaloPUCorr,
##         cutMuonLooseIDVeto,
##         cutSecMuonLooseIDVeto,
    )
)


PreSelPMissInvVetoIdMuon = cms.PSet(
    name = cms.string("PreSelPMissInvVetoIdMuon"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
        cutJetJetDPhi,
        cutTrkMuonId, 
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
        cutTrkRelIsoRp3,  
        cutTrkJetDeltaR,
        cutElecLooseIDVeto,
        cutTauLooseHadronicVeto,    
        cutTrkHitMissOut,
        cutMaxCaloPUCorr,
        cutMuonLooseIDVetoInv,
    )
)

PreSelInvVetoIdMuon = cms.PSet(
    name = cms.string("PreSelInvVetoIdMuon"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelInvMuonVeto.cuts),
    )
PreSelInvVetoIdMuon.cuts.append(cutTrkMuonId)


PreSelectionPMissing = cms.PSet(
    name = cms.string("PreSelectionPMissing"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPMissing.cuts.append(cutTrkHitMissOut)

PreSelNoTauVetoPMissing = cms.PSet(
    name = cms.string("PreSelNoTauVetoPMissing"),
    cuts = copy.deepcopy(PreSelNoTauVeto.cuts),
    )
PreSelNoTauVetoPMissing.cuts.append(cutTrkHitMissOut)


PreSelectionPMissingWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPSumPtLessThan = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThan"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPSumPtLessThan.cuts.append(cutTrkSumPtLT)

PreSelectionPSumPtLessThanWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThanWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtLessThan.cuts),
    )
PreSelectionPSumPtLessThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPSumPtLessThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPSumPtLessThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtLessThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtLessThanWithTrigJetMet.cuts),
    )
PreSelectionPSumPtLessThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPSumPtGreaterThan = cms.PSet(
    name = cms.string("PreSelectionPSumPtGreaterThan"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPSumPtGreaterThan.cuts.append(cutTrkSumPtGT)

PreSelectionPSumPtGreaterThanWithTrigJetMet = cms.PSet(
            name = cms.string("PreSelectionPSumPtGreaterThanWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionPSumPtGreaterThan.cuts),
            )
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPSumPtGreaterThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPSumPtGreaterThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPSumPtGreaterThanWithTrigJetMet.cuts),
    )
PreSelectionPSumPtGreaterThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingSumPtGreaterThan = cms.PSet(
        name = cms.string("PreSelectionPMissingSumPtGreaterThan"),
        cuts = copy.deepcopy(PreSelectionPMissing.cuts),
        )
PreSelectionPMissingSumPtGreaterThan.cuts.append(cutTrkSumPtGT)


PreSelectionPMissingSumPtGreaterThanWithTrigJetMet = cms.PSet(
        name = cms.string("PreSelectionPMissingSumGreaterThanWithTrigJetMet"),
            triggers = triggersJetMet,
            cuts = copy.deepcopy(PreSelectionPMissingSumPtGreaterThan.cuts),
            )
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingSumPtGreaterThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumGreaterThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtGreaterThanWithTrigJetMet.cuts),
    )
PreSelectionPMissingSumPtGreaterThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingSumPtLessThan = cms.PSet(
    name = cms.string("PreSelectionPMissingSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingSumPtLessThan.cuts.append(cutTrkSumPtLT)

PreSelectionPMissingSumPtLessThanWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumLessThanWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtLessThan.cuts),
    )
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts.insert(0,cutMET)

PreSelectionPMissingSumPtLessThanBlindWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionPMissingSumLessThanBlindWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionPMissingSumPtLessThanWithTrigJetMet.cuts),
    )
PreSelectionPMissingSumPtLessThanBlindWithTrigJetMet.cuts.append(cutMaxCaloPUCorrBlind)



PreSelectionPMissingDzSide = cms.PSet(
    name = cms.string("PreSelectionPMissingDzSide"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyDzSide.cuts),
    )
PreSelectionPMissingDzSide.cuts.append(cutMuonVeto)
PreSelectionPMissingDzSide.cuts.append(cutElecVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkDeadEcalVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkCrackVeto)
PreSelectionPMissingDzSide.cuts.append(cutTrkHitMissOut)

PreSelectionPMissingD0Side = cms.PSet(
    name = cms.string("PreSelectionPMissingD0Side"),
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyD0Side.cuts),
    )
PreSelectionPMissingD0Side.cuts.append(cutMuonVeto)
PreSelectionPMissingD0Side.cuts.append(cutElecVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkDeadEcalVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkCrackVeto)
PreSelectionPMissingD0Side.cuts.append(cutTrkHitMissOut)


## Preselection (AOD)
PreSelectionNoHitCut = cms.PSet(
    name = cms.string("PreSelectionNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       cutMuonVeto,
       cutElecVeto,
       cutTrkDeadEcalVeto,
       cutTrkCrackVeto,
       ),
    )
PreSelectionNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionNoHitCut.cuts),
    )
PreSelectionNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionIsoTrkOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       ),
    )

PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionIsoTrkOnlyNoHitCut.cuts),
    )
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionIsoTrkOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)


PreSelectionMuonVetoOnlyNoHitCut = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCut"),
    cuts = cms.VPSet (
       cutTrkPt,
       cutTrkEta,
       cutTrkD0,
       cutTrkDZ,
       cutTrkNHits,
       cutTrkIso,
       cutMuonVeto,
       ),
    )
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet = cms.PSet(
    name = cms.string("PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelectionMuonVetoOnlyNoHitCut.cuts),
    )
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutJetPt)
PreSelectionMuonVetoOnlyNoHitCutWithTrigJetMet.cuts.insert(0,cutMET)



## Gen Matched Channels ##

## FullSelectionCharginoId = cms.PSet(
##     name = cms.string("FullSelectionCharginoId"),
##     cuts = copy.deepcopy(FullSelection.cuts),
##     )
FullSelectionCharginoId = copy.deepcopy(FullSelection) 
FullSelectionCharginoId.name = cms.string("FullSelectionCharginoId")
for i in range(0, len(FullSelectionCharginoId.cuts)):
    if FullSelectionCharginoId.cuts[i].cutString == cutTrkPt.cutString:
        idx = i
FullSelectionCharginoId.cuts.insert(idx, cutTrkCharginoId)

FullSelectionCharginoIdDeadEcalLast = copy.deepcopy(FullSelectionCharginoId) 
FullSelectionCharginoIdDeadEcalLast.name = cms.string("FullSelectionCharginoIdDeadEcalLast")  
for i in xrange(len(FullSelectionCharginoIdDeadEcalLast.cuts) - 1, -1, -1):
    if FullSelectionCharginoIdDeadEcalLast.cuts[i].cutString == cutTrkDeadEcalVeto.cutString:
        del FullSelectionCharginoIdDeadEcalLast.cuts[i]                
FullSelectionCharginoIdDeadEcalLast.cuts.append(cutTrkDeadEcalVeto)

FullSelectionCharginoIdNHitsLast = copy.deepcopy(FullSelectionCharginoId) 
FullSelectionCharginoIdNHitsLast.name = cms.string("FullSelectionCharginoIdNHitsLast")  
for i in xrange(len(FullSelectionCharginoIdNHitsLast.cuts) - 1, -1, -1):
    if FullSelectionCharginoIdNHitsLast.cuts[i].cutString == cutTrkNHits.cutString:
        del FullSelectionCharginoIdNHitsLast.cuts[i]                
FullSelectionCharginoIdNHitsLast.cuts.append(cutTrkNHits) 


PreSelectionCharginoId = cms.PSet(
    name = cms.string("PreSelectionCharginoId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionCharginoId.cuts.append(cutTrkCharginoId)


PreSelectionElectronId = cms.PSet(
    name = cms.string("PreSelectionElectronId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionElectronId.cuts.append(cutTrkElectronId)

PreSelMuonId = cms.PSet(
    name = cms.string("PreSelMuonId"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelMuonId.cuts.append(cutTrkMuonId)

PreSelectionElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionElectronIdWithTrigJetMet.cuts.append(cutTrkElectronId)


PreSelectionPionId = cms.PSet(
    name = cms.string("PreSelectionPionId"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionPionId.cuts.append(cutTrkPionId)

PreSelectionPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
PreSelectionPionIdWithTrigJetMet.cuts.append(cutTrkPionId)


PreSelectionNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionNotGenMatched"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
PreSelectionNotGenMatched.cuts.append(cutTrkNotGenMatched)


PreSelectionPMissingElectronId = cms.PSet(
    name = cms.string("PreSelectionPMissingElectronId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingElectronId.cuts.append(cutTrkElectronId)


PreSelectionPMissingElectronIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingElectronIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingElectronIdWithTrigJetMet.cuts.append(cutTrkElectronId)


PreSelectionPMissingPionId = cms.PSet(
    name = cms.string("PreSelectionPMissingPionId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingPionId.cuts.append(cutTrkPionId)

PreSelectionPMissingPionIdWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("PreSelectionPMissingPionIdWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
PreSelectionPMissingPionIdWithTrigJetMet.cuts.append(cutTrkPionId)


PreSelectionPMissingNotGenMatched = cms.PSet(
    name = cms.string("PreSelectionPMissingNotGenMatched"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingNotGenMatched.cuts.append(cutTrkNotGenMatched)


PreSelectionPMissingLtMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtMesonId.cuts.append(cutTrkLightMesonId)


PreSelectionPMissingKMesonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKMesonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKMesonId.cuts.append(cutTrkKMesonId)


PreSelectionPMissingLtBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingLtBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingLtBaryonId.cuts.append(cutTrkLightBaryonId)


PreSelectionPMissingKBaryonId = cms.PSet(
    name = cms.string("PreSelectionPMissingKBaryonId"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
PreSelectionPMissingKBaryonId.cuts.append(cutTrkKBaryonId)


## Signal Region Channels ##

SigRegWithMaxCaloByPLoose = cms.PSet(
    name = cms.string("SigRegWithMaxCaloByPLoose"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloByPLoose.cuts.append(cutMaxCaloByPLoose)


SigRegWithMaxCaloByPLooseWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloByPLooseWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloByPLooseWithTrigJetMet.cuts.append(cutMaxCaloByPLoose)


SigRegWithMaxCaloByP = cms.PSet(
    name = cms.string("SigRegWithMaxCaloByP"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloByP.cuts.append(cutMaxCaloByP)


SigRegWithMaxCalo = cms.PSet(
    name = cms.string("SigRegWithMaxCalo"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
)
SigRegWithMaxCalo.cuts.append(cutMaxCaloTight)

PreSelWithMaxCalo = cms.PSet(
    name = cms.string("PreSelWithMaxCalo"),
    cuts = copy.deepcopy(PreSelection.cuts),
)
PreSelWithMaxCalo.cuts.append(cutMaxCaloTight) 
#PreSelWithMaxCalo.cuts.append(cutMaxMissOut)  # for data only


SigRegWithMaxCaloLoose = cms.PSet(
    name = cms.string("SigRegWithMaxCaloLoose"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloLoose.cuts.append(cutMaxCaloLoose)


SigRegWithMaxCaloLooseWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloLooseWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloLooseWithTrigJetMet.cuts.append(cutMaxCaloLoose)


SigRegNominal = cms.PSet(
    name = cms.string("SigRegNominal"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegNominal.cuts.append(cutMaxCalo10) 
SigRegNominal.cuts.append(cutTrkWheel0GapVeto) 
SigRegNominal.cuts.append(cutTrkEtaMuonPk)  

SigRegWithMaxCaloPUCorr = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorr"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorr.cuts.append(cutMaxCalo10)

SigRegWithMaxCaloPUCorrNoiseCleaned = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorrNoiseCleaned"),
    cuts = copy.deepcopy(PreSelectionWithNoiseClean.cuts),
    )
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutTrkHitMissOut)
SigRegWithMaxCaloPUCorrNoiseCleaned.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrAndSumPtLessThan = cms.PSet(
    name = cms.string("SigRegWithMaxCaloPUCorrAndSumPtLessThan"),
    cuts = copy.deepcopy(PreSelectionPMissing.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrAndSumPtLessThan.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorrWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloPUCorrWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)

SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet = cms.PSet(
    triggers = triggersJetMet,
    name = cms.string("SigRegWithMaxCaloPUCorAndSumPtLessThanWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionPMissingWithTrigJetMet.cuts),
    )
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutTrkSumPtLT)
SigRegWithMaxCaloPUCorrAndSumPtLessThanWithTrigJetMet.cuts.append(cutMaxCaloPUCorr)


## Control Region Channels ##
CtrlReg = cms.PSet(
    name = cms.string("CtrlReg"),
    cuts = copy.deepcopy(PreSelection.cuts),
    )
CtrlReg.cuts.append(cutTrkHitMissOutCtrlReg)


CtrlRegWithTrigJetMet = cms.PSet(
    name = cms.string("CtrlRegWithTrigJetMet"),
    cuts = copy.deepcopy(PreSelectionWithTrigJetMet.cuts),
    )
CtrlRegWithTrigJetMet.cuts.append(cutTrkHitMissOutCtrlReg)


JetFirst = cms.PSet(
    name = cms.string("JetFirst"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutJetPt,
        cutMET,
        )
    )

MetFirst = cms.PSet(
    name = cms.string("MetFirst"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        )
    )

TrigTestTighterMet = cms.PSet(
    name = cms.string("TrigTestTighterMet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cms.PSet (
            inputCollection = cms.string("mets"),
            cutString = cms.string("pt > 250"),
            numberRequired = cms.string(">= 1"),
            ),
        cutJetPt,
        )
    )

TrigTestTighterJet = cms.PSet(
    name = cms.string("TrigTestTighterJet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cms.PSet (
            inputCollection = cms.string("jets"),
            cutString = cms.string("pt > 180"),
            numberRequired = cms.string(">= 1"),
            ),
        )
    )


JetOnly = cms.PSet(
    name = cms.string("JetOnly"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
        cutJetNoiseChgHad,
        cutJetNoiseNeuEM,
        cutJetNoiseNeuHad,
       ),
    )

JetOnlyNoClean = cms.PSet(
    name = cms.string("JetOnlyNoClean"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutJetPt,
        cutJetEta,
       ),
    )


# Monojet selection #  
MonoJet = cms.PSet(
    name = cms.string("MonoJet"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
#        cutMET200,
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
#        cutJetPt,
#        cutJetEta2p4,
#        cutJetNoiseChgHad,
#        cutJetNoiseChgEM,
#        cutJetNoiseNeuEM,
#        cutJetNoiseChgEM,
#        cutLeadingJetID,
        cutSubLeadingJetID,
        cutNJets,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
#        cutSecJetNoiseChgHad,
#        cutSecJetNoiseChgEM,
#        cutSecJetNoiseNeuHad,
#        cutSecJetNoiseNeuEM,
#        cutSecJetPt,
#        cutSecJetEta2p4,
#        cutNJets,
#        cutJetJetDPhi,
#        cutMuonVeto,
#        cutElecVeto,
#        cutTauVeto,
       ),
    )

# Modified Monojet selection #  
MonoJetNoNJetVeto = cms.PSet(
    name = cms.string("MonoJetNoNJetVeto"),
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
#        cutNJets,
        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
       ),
    )

# Modified Monojet selection #  
MonoJetNoSubjetCuts = cms.PSet(
    name = cms.string("MonoJetNoSubjetCuts"),  
    triggers = triggersJetMet,
    cuts = cms.VPSet (
        cutMET,
        cutSecJetPt,
        cutSecJetEta2p4,            
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutSubLeadingJetID,
#        cutNJets,
#        cutJetJetDPhi,
        cutElecLooseIDVeto,
        cutMuonLooseIDVeto,
        cutTauLooseHadronicVeto,
        cutTrkPt,
        cutTrkEta,
        cutTrkD0,
        cutTrkDZ,
        cutTrkNHits,
        cutTrkHitMissMid,
        cutTrkHitMissIn,
#        cutTrkIso,
        cutTrkDeadEcalVeto,
        cutTrkCrackVeto,
       ),
    )


AtlasDisappTrk = cms.PSet(
    # Copy cuts from arXiv:1210.2852v1, JHEP 01 (2013) 131
    # and PRD 88, 112006 (2013)  
    name = cms.string("AtlasDisappTrk"),
    # Do not apply a trigger  
    cuts = cms.VPSet (
        cutEvtFilter,
        cutVtxGood, 
        cutSecJetEta2p8,
        cutSecJetNoiseChgHad,
        cutSecJetNoiseChgEM,
        cutSecJetNoiseNeuHad,
        cutSecJetNoiseNeuEM,
        cutElecVetoPt10, 
        cutMuonVetoPt10,
        cutSecMuonVetoPt10,
        cutSecJetPt90,
        cutMET90,
        cutMetDeltaPhiMin2Jets, 
        cutTrkPt15,
        # Missing:  highest-pt isolated track 
        cutTrkEtaAtlas,
        # Missing:  N_b-layer >= 1
        # Missing:  N_pixel >= 3
        # Missing:  N_SCT >= 2
        cutTrkNHits,
        cutTrkHitMissIn,
        cutTrkHitMissMid,
        cutTrkD0Atlas,
        cutTrkDZSinTheta,
        # Missing:  track chi2 prob > 10%  
        cutTrkChi2Norm1p6,
        #        cutTrkPtError,
        cutTrkRelIsoRp3Atlas, 
        cutTrkJetDeltaRAtlas,
        cutTrkDeadEcalVeto, 
        cutTrkHitMissOut,
        cutTrkPt75, 
       )  
    )

AtlasDisappTrkUptoMet = cms.PSet(
    name = cms.string("AtlasDisappTrkUptoMet"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
# remove the cuts after the Met cut
for i in range(0, len(AtlasDisappTrkUptoMet.cuts)):  
    if AtlasDisappTrkUptoMet.cuts[i].cutString == cutMET90.cutString:
        idx = i
del AtlasDisappTrkUptoMet.cuts[idx+1:len(AtlasDisappTrkUptoMet.cuts)]  

AtlasDisappTrkIsoTrk = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrk"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
# remove the last two cuts 
del AtlasDisappTrkIsoTrk.cuts[len(AtlasDisappTrkIsoTrk.cuts)-1]
del AtlasDisappTrkIsoTrk.cuts[len(AtlasDisappTrkIsoTrk.cuts)-1]


AtlasDisappTrkIsoTrkMissOut3 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut3"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut3.cuts.append(cutTrkHitMissOut) 

AtlasDisappTrkIsoTrkMissOut6 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut6"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut6.cuts.append(cutTrkHitMissOut6) 

AtlasDisappTrkIsoTrkMissOut7 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut7"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut7.cuts.append(cutTrkHitMissOut7) 

AtlasDisappTrkIsoTrkMissOut8 = cms.PSet(
    name = cms.string("AtlasDisappTrkIsoTrkMissOut8"),
    cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
    )
AtlasDisappTrkIsoTrkMissOut8.cuts.append(cutTrkHitMissOut8) 

## AtlasDisappTrkIsoTrkDeadEcal = cms.PSet(
##     name = cms.string("AtlasDisappTrkIsoTrkDeadEcal"),
##     cuts = copy.deepcopy(AtlasDisappTrkIsoTrk.cuts),
##     )
## AtlasDisappTrkIsoTrkDeadEcal.cuts.append(cutTrkDeadEcalVeto)  

AtlasDisappTrkTrigMet = cms.PSet(
    name = cms.string("AtlasDisappTrkTrigMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkTrigMet.cuts.append(cutMET)  

AtlasDisappTrkDeadEcal = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcal"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkDeadEcal.cuts.append(cutTrkDeadEcalVeto)  

AtlasDisappTrkDeadEcalMuonCuts = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalMuonCuts"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcal.cuts),
    )
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutSecMuonVetoPt10)
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutTrkWheel0GapVeto)
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutTrkEtaMuonPk)
AtlasDisappTrkDeadEcalMuonCuts.cuts.append(cutTrkBadCSCVeto)  

AtlasDisappTrkDeadEcalSecMuonVeto = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalSecMuonVeto"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcal.cuts),
    )
AtlasDisappTrkDeadEcalSecMuonVeto.cuts.append(cutSecMuonVetoPt10)

AtlasDisappTrkDeadEcalSecMuonVetoEcalo = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalSecMuonVetoEcalo"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcalSecMuonVeto.cuts),
    )
AtlasDisappTrkDeadEcalSecMuonVetoEcalo.cuts.append(cutMaxCalo10)

AtlasDisappTrkDeadEcalEtaVeto = cms.PSet(
    name = cms.string("AtlasDisappTrkDeadEcalEtaVeto"),
    cuts = copy.deepcopy(AtlasDisappTrkDeadEcal.cuts),
    )
AtlasDisappTrkDeadEcalEtaVeto.cuts.append(cutTrkEtaAtlasVeto)  

AtlasDisappTrkCharginoId = cms.PSet(
    name = cms.string("AtlasDisappTrkCharginoId"),
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkCharginoId.cuts.insert(8,cutTrkCharginoId)  

AtlasDisappTrkCharginoIdTrigMet = cms.PSet(
    # add trigger and Met cut 
    name = cms.string("AtlasDisappTrkCharginoIdTrigMet"),
    triggers = triggersJetMet,
    cuts = copy.deepcopy(AtlasDisappTrk.cuts),
    )
AtlasDisappTrkCharginoIdTrigMet.cuts.append(cutMET)  





