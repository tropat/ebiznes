package controllers

import javax.inject._
import play.api.mvc._

@Singleton
class Cart @Inject()(val controllerComponents: ControllerComponents) extends BaseController {
  private var cart: List[String] = List("item_1", "item_2", "item_3", "item_4")

  def getAllCartItems: Action[AnyContent] = Action {
    Ok(cart.mkString(" "))
  }

  def getCartItemById(id: Int): Action[AnyContent] = Action {
    cart.lift(id - 1) match {
      case Some(item) => Ok(item)
      case None => NotFound("Item not found")
    }
  }

  def updateCartItem(id: Int): Action[AnyContent] = Action {
    cart.lift(id - 1) match {
      case Some(_) =>
        Ok(s"Item $id updated")
      case None => NotFound("Item not found")
    }
  }

  def deleteCart(id: Int): Action[AnyContent] = Action {
    cart.lift(id - 1) match {
      case Some(_) =>
        cart = cart.filterNot(_ == cart(id - 1))
        Ok(s"Item $id deleted")
      case None => NotFound("Item not found")
    }
  }

  def addCartItem: Action[AnyContent] = Action {
    val newItem = s"${cart.length + 1}"
    cart = cart :+ newItem
    Ok(s"Item added: $newItem")
  }
}
