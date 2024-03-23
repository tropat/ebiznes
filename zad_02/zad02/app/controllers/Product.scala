package controllers

import javax.inject._
import play.api.mvc._

@Singleton
class Product @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
  private var products: List[String] = List("1", "2", "3", "4", "5", "6", "7", "8")

  def getAllProducts: Action[AnyContent] = Action {
    Ok(products.mkString(" "))
  }

  def getProductById(id: Int): Action[AnyContent] = Action {
    products.lift(id - 1) match {
      case Some(product) => Ok(product)
      case None => NotFound("Product not found")
    }
  }

  def updateProduct(id: Int): Action[AnyContent] = Action {
    products.lift(id - 1) match {
      case Some(_) =>
        Ok(s"Product $id updated")
      case None => NotFound("Product not found")
    }
  }

  def deleteProduct(id: Int): Action[AnyContent] = Action {
    products.lift(id - 1) match {
      case Some(_) =>
        products = products.filterNot(_ == products(id - 1))
        Ok(s"Product $id deleted")
      case None => NotFound("Product not found")
    }
  }

  def addProduct: Action[AnyContent] = Action {
    val newProduct = s"${products.length + 1}"
    products = products :+ newProduct
    Ok(s"Product added: $newProduct")
  }
}
