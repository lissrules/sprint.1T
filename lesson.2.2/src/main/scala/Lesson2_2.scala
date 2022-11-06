import scala.io.StdIn.readLine
object Lesson2_2 {
  var iAccYear = -1
  var iBonusYear = -1
  var iEatYear = -1
  val dNalog = 0.42
  var lOklads : List [Int] = List(100, 150, 200, 80, 120, 75)

  def fHello(): Unit ={
    val str = "Hello world!"
    println(str)
    println(str.reverse)
    println(str.toLowerCase())
    println(str.replace("!", ""))
    println(str.replace("!", "") + " and goodbye python!")
  }
  def fInput(str : String):Int ={
    println(str)
    return readLine().toInt
  }
  def fOklad(): Unit = {
    val iAcc =  fInput("Годовой доход:")
    iAccYear = iAcc
    val iAmountBonus = fInput("Премия, %:")
    iBonusYear = iAmountBonus
    val iAmountEat = fInput("Компенсация питания:")
    iEatYear = iAmountEat
    var dAmount:Double = (iAcc + iAcc*iAmountBonus/100 + iAmountEat)
    dAmount = (dAmount - dAmount*dNalog)/12
    println(f"Ежемесячный оклад после вычета доходов : $dAmount%1.2f")
  }
  def fDiffOkl():Unit = {
    if (iAccYear == -1 || iBonusYear == -1 || iEatYear == -1) {
      println("Не все данные были заполнены во 2 задаче")
      return
    }
    val lOklads_ = lOklads :+ iAccYear
    val iMean :Int = lOklads.sum/lOklads.size
    println(f"Среденее значение $iMean для списка $lOklads")
    println("Расхождение зарплат со средним по списку в % отношении")
    println( lOklads_.map(x => ((x - iMean) * 100/ x)))
  }
  def fAddOkl():Unit ={
    println(f"Текущий список окладов $lOklads")
    val lOklads_ = lOklads :+ fInput("Введите новый оклад")
    println(f"Текущий список окладов $lOklads_")
    println(f"Минимальная позиция в списке ${lOklads_.min}")
    println(f"Максимальная позиция в списке ${lOklads_.max}")
    lOklads = lOklads_
  }
  def fSortOkl():Unit = {
    println(f"Текущий список окладов $lOklads")
    val lAdd = List (350, 90)
    val lNewList = lOklads ++ lAdd
    println(f"Cписок окладов $lNewList после объединения со списком $lAdd")
    lOklads = lNewList.sorted
    println(f"Cписок отсортированных окладов $lOklads")
  }
  def fInsertOkl():Unit = {
    println(f"Текущий список окладов $lOklads")
    val iInsItem = fInput("Введите оклад для вставки")
    val (lBefore, lAfter) = lOklads.span(_ < iInsItem)
    lOklads = (lBefore :+ iInsItem) ++ lAfter
    println(f"Новый список окладов $lOklads")
  }
  def fMiddleOkl(): Unit = {
    var lMiddle : List[Int] = List()
    println(f"Текущий список окладов $lOklads")
    val iLow = fInput("Введите нижнюю границу оклада")
    val iHigh = fInput("Введите верхнюю границу оклада")
    for (item <- lOklads) if ((iLow <= item) && (item <= iHigh)) lMiddle = lMiddle :+ lOklads.indexOf(item)
    println(f"Индексы сотрудникоы $lMiddle")
  }
  def fIndexOkl(): Unit = {
    println(f"Текущий список окладов $lOklads")
    println(lOklads.map(x => (x * 1.07).toInt))
  }

  def main(args: Array[String]): Unit={
    var iChoice: String = ""
    while (iChoice != "0" ) {
      println("Введите букву задачи для показа решения или 0 для выхода")
      iChoice = readLine().toLowerCase
      iChoice match {
        case "0" => return
        case "a" => fHello()
        case "b" => fOklad()
        case "c" => fDiffOkl()
        case "d" => fAddOkl()
        case "e" => fSortOkl()
        case "f" => fInsertOkl()
        case "g" => fMiddleOkl()
        case "h" => fIndexOkl()
      }
    }
  }
}
