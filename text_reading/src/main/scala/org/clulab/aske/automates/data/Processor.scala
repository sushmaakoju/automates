package org.clulab.aske.automates.data

trait Preprocessor {
  def cleanUp(text: String): String
}

class EdgeCaseParagraphPreprocessor() extends Preprocessor {
  def cleanUp(text: String): String = {
    val digits = "0123456789"
    val numberOfDigits = text.filter(c => digits.contains(c)).length
    val digitThreshold = 0.25
    text match {
      case text if numberOfDigits.toDouble / text.split(" ").length > digitThreshold => {
        println("Filtering bc the value is: " + numberOfDigits.toDouble / text.split(" ").length )
        val cleanedUpText = text.replaceAll(" \\d+", ".")
        cleanedUpText
      }
      case _ => {
        println("NOT filtering bc the value is: " + numberOfDigits.toDouble / text.split(" ").length )
        text} //todo: add other clean up, e.g., in-paragraph tables
    }
  }
}

object EdgeCaseParagraphPreprocessor {
  def apply(): EdgeCaseParagraphPreprocessor = new EdgeCaseParagraphPreprocessor()

}


class PassThroughPreprocessor() extends Preprocessor {
  def cleanUp(text: String): String = {
    text
  }
}

object PassThroughPreprocessor {
  def apply(): PassThroughPreprocessor = new PassThroughPreprocessor

}