describe('cone.example', () => {
    it('successfully loads', () => {
      cy.visit('/')
    })
})

describe('Login', () => {
    it('get login fields', () => {
        cy.get('#form-loginform')
        cy.get('#input-loginform-user')
        cy.get('#input-loginform-password')
        cy.get('#input-loginform-login')
    })
    it('type login', () => {
        cy.get('#input-loginform-user').type('admin')
        cy.get('#input-loginform-password').type('admin')
        cy.get('#input-loginform-login').click()
    })
})

describe('Topnav', () => {
    context('desktop resolution', () => {
      beforeEach(() => {
        // run desktop resolution tests
        cy.viewport(2000, 1000)
      })
  
      it('topnav content visible & topnav class not mobile', () => {
        cy.get('#topnav').should('not.have.class', 'mobile')
        cy.get('#topnav-content').should('have.css', 'display')
        .and('match', /contents/)
      })
      it('dropdowns hidden', () => {
          cy.get('.cone-mainmenu-dropdown').should('be.hidden')
          cy.get('.dropdown-menu').should('be.hidden')
      })
    })
  
    context('mobile resolution', () => {
      beforeEach(() => {
        // run mobile resolution tests
        cy.viewport('iphone-5')
      })
  
      it('mobile content hidden & topnav class mobile', () => {
        cy.get('#topnav').should('have.class', 'mobile')
        cy.get('#topnav-content').should('be.hidden')
      })
      it('dropdowns hidden', () => {
          cy.get('.dropdown').should('be.hidden')
      })

      it('clicked toggle btn, menu visible', () => {
          cy.get('#mobile-menu-toggle').click()
          cy.get('#topnav-content').should('be.visible')
          cy.get('#mobile-menu-toggle').click()
          cy.get('#topnav-content').should('be.hidden')
      })
    }) 
})