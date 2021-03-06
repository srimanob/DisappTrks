#!/usr/bin/env python

from DisappTrks.StandardAnalysis.closureTest import *  
from DisappTrks.StandardAnalysis.getUser import * 
from ROOT import TCanvas, TFile, gROOT 
import os 


dirs = getUser() 

gROOT.SetBatch()
canvas = TCanvas("c1", "c1",800,800)
setCanvasStyle(canvas)


print "********************************************************************************"
print "performing electron background closure test with sum of TTJets and WJetsToLNu..."
print "--------------------------------------------------------------------------------"
sample = "bkgd_TT_WJets" 
condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets"
fout = TFile.Open ("elecBkgdClosureTest_TT_WJets.root", "recreate")
elecBkgdClosureTest_TT_WJets = LeptonBkgdClosureTest ("electron")
elecBkgdClosureTest_TT_WJets.addTFile (fout)
elecBkgdClosureTest_TT_WJets.addTCanvas (canvas)
elecBkgdClosureTest_TT_WJets.addMetCut (100.0)
elecBkgdClosureTest_TT_WJets.addChannel  ("TagProbe",            "ZtoEleProbeTrkWithZCuts", "DYJetsToLL_50", dirs['Wells']+"electronTagProbe") 
elecBkgdClosureTest_TT_WJets.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            "DYJetsToLL_50", dirs['Wells']+"electronTagProbe") 
elecBkgdClosureTest_TT_WJets.addChannel  ("TagPt35",             "ElectronTagPt35",        sample, dirs['Wells']+'ElectronTagPt35')  
elecBkgdClosureTest_TT_WJets.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig", sample, dirs['Wells']+"ElectronTagPt35MetTrig")  
elecBkgdClosureTest_TT_WJets.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",      sample+"HT", condor_dir)
elecBkgdClosureTest_TT_WJets.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet", sample, condor_dir)
elecBkgdClosureTest_TT_WJets.printStdResults()  
fout.Close()  

print "\n\n"
print "********************************************************************************"
print "performing electron background closure test with TTJets..."
print "--------------------------------------------------------------------------------"
sample = "TTJets"
condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets" 
fout = TFile.Open ("elecBkgdClosureTest_TTJets.root", "recreate")
elecBkgdClosureTest_TTJets = LeptonBkgdClosureTest ("electron")
elecBkgdClosureTest_TTJets.addTFile (fout)
elecBkgdClosureTest_TTJets.addTCanvas (canvas)
elecBkgdClosureTest_TTJets.addMetCut (100.0)
elecBkgdClosureTest_TTJets.addChannel  ("TagProbe",            "ZtoEleProbeTrkWithZCuts", "DYJetsToLL_50", dirs['Wells']+"electronTagProbe") 
elecBkgdClosureTest_TTJets.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            "DYJetsToLL_50", dirs['Wells']+"electronTagProbe") 
elecBkgdClosureTest_TTJets.addChannel  ("TagPt35",             "ElectronTagPt35",        sample, dirs['Wells']+'ElectronTagPt35')  
elecBkgdClosureTest_TTJets.addChannel  ("TagPt35NoTrig",       "ElectronTagPt35NoTrig",  sample, condor_dir)   
elecBkgdClosureTest_TTJets.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig", sample, dirs['Wells']+"ElectronTagPt35MetTrig")  
elecBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",      sample, condor_dir)
elecBkgdClosureTest_TTJets.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet", sample, condor_dir)
elecBkgdClosureTest_TTJets.printStdResults()  
fout.Close()  


print "\n\n"
print "********************************************************************************"
print "performing electron background closure test with WJetsToLNu..."
print "--------------------------------------------------------------------------------"
sample = "WJetsToLNu"
condor_dir = dirs['Wells']+"ElecBkgdClosureTestWjets"
fout = TFile.Open ("elecBkgdClosureTest_WJetsToLNu.root", "recreate")
elecBkgdClosureTest_WLNu = LeptonBkgdClosureTest ("electron")
elecBkgdClosureTest_WLNu.addTFile (fout)
elecBkgdClosureTest_WLNu.addTCanvas (canvas)
elecBkgdClosureTest_WLNu.addMetCut (100.0)
elecBkgdClosureTest_WLNu.addChannel  ("TagProbe",            "ZtoEleProbeTrkWithZCuts", "DYJetsToLL_50", dirs['Wells']+"electronTagProbe") 
elecBkgdClosureTest_WLNu.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            "DYJetsToLL_50", dirs['Wells']+"electronTagProbe") 
elecBkgdClosureTest_WLNu.addChannel  ("TagPt35",             "ElectronTagPt35",        sample, dirs['Wells']+'ElectronTagPt35')  
elecBkgdClosureTest_WLNu.addChannel  ("TagPt35NoTrig",       "ElectronTagPt35NoTrig",  sample, condor_dir)   
elecBkgdClosureTest_WLNu.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig", sample, dirs['Wells']+"ElectronTagPt35MetTrig")  
elecBkgdClosureTest_WLNu.addChannel  ("CandTrkIdPt35",       "CandTrkIdElecPt35",      sample+"_HT", condor_dir)
elecBkgdClosureTest_WLNu.addChannel  ("CandTrkIdPt35NoMet",  "CandTrkIdElecPt35NoMet", sample, condor_dir)
elecBkgdClosureTest_WLNu.printStdResults()  
fout.Close()  


print "\n\n"
print "********************************************************************************"
print "performing electron background estimate for data in Disappearing Track sample..."
print "--------------------------------------------------------------------------------"
sample = "SingleEle_2015D"
fout = TFile.Open ("elecBkgdClosureTest_Data.root", "recreate")
elecBkgdClosureTest_Data = LeptonBkgdClosureTest ("electron")
elecBkgdClosureTest_Data.addTFile (fout)
elecBkgdClosureTest_Data.addTCanvas (canvas)
elecBkgdClosureTest_Data.addMetCut (100.0) 
elecBkgdClosureTest_Data.addChannel  ("TagProbe",            "ZtoEleProbeTrkWithZCuts", sample, dirs['Wells']+"ZtoEleProbeTrkWithZCuts") 
elecBkgdClosureTest_Data.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            sample, dirs['Wells']+"ZtoEleDisTrk")  
# elecBkgdClosureTest_Data.addChannel  ("TagPt35",             "ElectronTagPt35",        sample, dirs['Wells']+'ElectronTagPt35')  
# elecBkgdClosureTest_Data.addChannel  ("TagPt35MetTrig",      "ElectronTagPt35MetTrig", sample, dirs['Wells']+"ElectronTagPt35")  
elecBkgdClosureTest_Data.addChannel  ("TagPt35",             "ElectronTagPt50",         sample, dirs['Wells']+'ElecBkgdEstimateWithJetCuts')  
elecBkgdClosureTest_Data.addChannel  ("TagPt35MetTrig",      "ElectronTagPt50MetTrig",  sample, dirs['Wells']+"ElecBkgdEstimateWithJetCuts")  
elecBkgdClosureTest_Data.printStdResults()  
fout.Close()  

print "\n\n"
print "********************************************************************************"
print "performing electron background estimate for data in Candidate Track sample..."
print "--------------------------------------------------------------------------------"
elecBkgdClosureTest_Data.addChannel  ("TagProbePass",        "ZtoEleCandTrk",  sample, "ElecTagProbeChannels")  
elecBkgdClosureTest_Data.printStdResults()  

print "\n\n"
print "********************************************************************************"
print "performing electron background estimate for data in Ecalo Sdband sample..."
print "--------------------------------------------------------------------------------"
elecBkgdClosureTest_Data.addChannel  ("TagProbePass",        "ZtoEleCandTrkSdbandEcalo",  sample, dirs['Wells']+"ElecTagProbeChannels")  
elecBkgdClosureTest_Data.printStdResults()  

print "\n\n"
print "********************************************************************************"
print "performing electron background estimate for data in NMissOut Sdband sample..."
print "--------------------------------------------------------------------------------"
elecBkgdClosureTest_Data.addChannel  ("TagProbePass",        "ZtoEleCandTrkSdbandNMissOut", sample, dirs['Wells']+"ElecTagProbeChannels")  
elecBkgdClosureTest_Data.printStdResults()  

print "\n\n"
print "********************************************************************************"
print "performing electron background estimate for data in Disappearing Track sample (no NMissOut cut)..."
print "--------------------------------------------------------------------------------"
elecBkgdClosureTest_Data.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            sample, dirs['Wells']+"ElecTagProbeChannels")  # No NMissOut cut 
elecBkgdClosureTest_Data.printStdResults()  

print "\n\n"
print "********************************************************************************"
print "performing electron background estimate for data in Disappearing Track sample..."
print "--------------------------------------------------------------------------------"
elecBkgdClosureTest_Data.addChannel  ("TagProbePass",        "ZtoEleDisTrk",            sample, dirs['Wells']+"ZtoEleDisTrk") 
elecBkgdClosureTest_Data.printStdResults()  



