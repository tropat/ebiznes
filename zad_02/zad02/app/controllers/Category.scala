package controllers

import javax.inject._
import play.api.mvc._

@Singleton
class Category @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
  private var categories: List[String] = List("category_1", "category_2", "category_3", "category_4")

  def getAllCategories: Action[AnyContent] = Action {
    Ok(categories.mkString(" "))
  }

  def getCategoryById(id: Int): Action[AnyContent] = Action {
    categories.lift(id - 1) match {
      case Some(category) => Ok(category)
      case None => NotFound("Category not found")
    }
  }

  def updateCategory(id: Int): Action[AnyContent] = Action {
    categories.lift(id - 1) match {
      case Some(_) =>
        Ok(s"Category $id updated")
      case None => NotFound("Category not found")
    }
  }

  def deleteCategory(id: Int): Action[AnyContent] = Action {
    categories.lift(id - 1) match {
      case Some(_) =>
        categories = categories.filterNot(_ == categories(id - 1))
        Ok(s"Category $id deleted")
      case None => NotFound("Category not found")
    }
  }

  def addCategory: Action[AnyContent] = Action {
    val newCategory = s"${categories.length + 1}"
    categories = categories :+ newCategory
    Ok(s"Category added: $newCategory")
  }
}
