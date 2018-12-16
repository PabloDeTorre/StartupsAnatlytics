package com.sparkTutorial.sparkSql.kickstarter

import org.apache.log4j.{Level, Logger}
import org.apache.spark.{SparkConf, SparkContext}


object kickstarter {

  val PRICE_SQ_FT = "Price SQ Ft"

  def main(args: Array[String]) {

    Logger.getLogger("org").setLevel(Level.ERROR)

    val conf = new SparkConf().setAppName("airportLatitude").setMaster("local[2]")
    val sc = new SparkContext(conf)

    val lines = sc.textFile("in/kickstarter.csv")

    val header = lines.first()
    val cleanLinesHeader = lines.filter(x => x != header)

    //(11) country - (2) category - (14) usd_goal_real - (13) usd_pledged_real

    val focusColumns = cleanLinesHeader.map(x => {

        val splits = x.split(",")
        splits(11) + "," + splits(2) + "," +splits(14) + "," + splits(13)

    })


    val filterCorrectLines = focusColumns.filter(x => x.split(",").length == 4)
    val filterCorrectDigit = filterCorrectLines.filter(x => {

      val filter = x.split(",")
      filter(3).isNumeric()

    })

    val result = filterCorrectDigit.filter(x => {

      val filter = x.split(",")
      filter(3).toFloat > 1000000

    })


    result.saveAsTextFile("out/kickstarter.txt")

  }

  implicit class OpsNum(val str: String) extends AnyVal {
    def isNumeric() = scala.util.Try(str.toFloat).isSuccess
  }

}



