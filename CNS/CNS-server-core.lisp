;Load modules
(ql:quickload '("hunchentoot" "caveman2" "cl-who" "spinneret"
                "djula" "easy-routes"))

;Set up acceptor and start listening on 4242..
(defvar *acceptor* (make-instance 'hunchentoot:easy-acceptor
                                  :port 4143))
(hunchentoot:start *acceptor*)

;Set another directory to serve pages from...
(setf (hunchentoot:acceptor-document-root *acceptor*)
      #p"/home/cryptao/Development/dev/CNS/index.html")

;;Example of using Hunchentoot and cl-who to generate content

(defpackage :webserver
  (:use :common-lisp :hunchentoot :cl-who))

(in-package :webserver)

;;(setf *dispatch-table*
;;      (list #'dispatch-easy-handlers
;;            #'default-dispatcher))

;;(setf *show-lisp-errors-p* t
;;      *show-lisp-backtraces-p* t)

(define-easy-handler (easy-demo :uri "/lisp/hello"
                                :default-request-type :get)
    ((state-variable :parameter-type 'string))
  (with-html-output-to-string (*standard-output* nil :prologue t)
    (:html
     (:head (:title "Hello, world!"))
     (:body
      (:h1 "This should display the number nine.."
	   (print (+ 4 5)))
      (:p "This is my Lisp web server, running on Hunchentoot,"
          " as described in "
          (:a :href
              "http://newartisans.com/blog_files/hunchentoot.primer.php"
              "this blog entry")
          " on Common Lisp and Hunchentoot.")))))
